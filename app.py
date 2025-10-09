import streamlit as st
import pandas as pd
from github import Github
from dotenv import load_dotenv
import datetime
import time
import os
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import requests
import zipfile
import io

load_dotenv()
token = os.getenv("NEW_TOKEN")
g = Github(token)
repo = g.get_repo("Office-of-Institutional-Effectiveness/oie-research-data")


# Get file contents from whole directory
@st.cache_data
def get_all_files_cached():
    files = repo.get_contents("")
    all_data = []

    def extract_files(contents):
        for content in contents:
            if content.type == "dir":
                extract_files(repo.get_contents(content.path))
            else:
                category = content.path.split("/")[0] if "/" in content.path else "else"
                commits = repo.get_commits(path=content.path)
                commits = repo.get_commits(path=content.path)
                last_commit = commits[0] if commits.totalCount > 0 else None

                last_modified_date = (
                    last_commit.commit.author.date.strftime('%Y-%m-%d')
                    if last_commit else "Unknown"
                )

                author = (
                    last_commit.author.login
                    if last_commit and last_commit.author else "Unknown"
                )

                all_data.append({
                    "File name": content.name,
                    "File Path": content.path,
                    "Category": category,
                    "Last modified date": last_modified_date,
                    "Author":author,
                    "Download": f"https://github.com/{repo.full_name}/blob/main/{content.path}"
                })

    extract_files(files)
    return all_data

# Load file data
file_data = get_all_files_cached()

# Create dataframe fo display
df = pd.DataFrame(file_data)
df = df[["File name","Author","Last modified date","File Path", "Category", "Download"]]

# st.title("OIE Data Storage")
st.markdown("""<h1 style='background-color:#e6f7ff; border-radius:15px; margin:5px;'> OIE Data Storage </div>""", unsafe_allow_html=True)

st.markdown("""<div style='margin:10px;'>Search, Preview, and Download Institutional Research Files </div>""", unsafe_allow_html=True)


# UI elements for category selection and search
col1, col2 = st.columns(2)

with col1:
    category_list = ["All"] + sorted(df["Category"].unique())
    selected_category = st.selectbox("📁 Select Project (Category)", category_list)

query = st.text_input("🔍 Search by Project/File name/Author/Date")

# Filtering and searching
filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

if query:
    query_lower = query.lower()
    filtered_df = filtered_df[
        filtered_df.apply(lambda row:
            query_lower in row["File name"].lower() or
            query_lower in row["File Path"].lower() or
            query_lower in row["Author"].lower() or
            query_lower in row["Last modified date"].lower() or
            query_lower in row["Category"].lower(), axis=1)
    ]

# Display search result in interactive table
gd = GridOptionsBuilder.from_dataframe(filtered_df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(filtered_df, height=500, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)



# Display selected files
# st.write('### Files Ready for Download')
st.markdown("<h4 style='color:#3366cc;'> Files Ready for Download </h3>", unsafe_allow_html=True)

selected_row = grid_table["selected_rows"]
st.dataframe(selected_row)

# Convert selected rows to dictionary
if selected_row is not None and not selected_row.empty:
    selected_row_dicts = selected_row.to_dict(orient="records")
else:
    selected_row_dicts = [] 

# Download selected files
headers = {"Authorization": f"token {token}"}
downloaded_files = []

for row in selected_row_dicts:
    file_path = row["File Path"]
    file_name = row["File name"]

    try:
        file_content = repo.get_contents(file_path)
        content_bytes = file_content.decoded_content
        downloaded_files.append((file_name, content_bytes))
    except Exception as e:
        st.warning(f"⚠️ Failed to fetch {file_name}: {e}")

# Create ZIP archive in memory
# This allows reading/writing binary data in RAM instead of saving to disk
if downloaded_files:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for file_name, content in downloaded_files:
            zip_file.writestr(file_name, content)
    zip_buffer.seek(0)

    # Show download button
    st.download_button(
        label="Download",
        data=zip_buffer,
        file_name="selected_files.zip",
        mime="application/zip"
    )
else:
    st.warning("No file selected")





