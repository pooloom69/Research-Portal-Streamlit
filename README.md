# StreamlitApp

# Office of Institutional Effectiveness

Welcome to the GitHub repository for storing, sharing, and managing institutional research project files at Fullerton College.
<br><br>
---
## This repository is designed to serve two primary purposes:

1. **Active collaboration** – Researchers can share, update, and manage files for ongoing projects.
2. **Reference archive** – Store and retrieve finalized documents from past research projects.
<br><br><br>

## Category Structure
Each **main folder** represents a project (e.g., `kpi_dashboard`, `enrollment_management`, etc.), and each includes the following standardized subfolders:

/project_name/<br>
├── sql/<br>
│ ├── raw/ # Initial or rough SQL queries<br>
│ └── cleaned/ # Finalized SQL queries for use or presentation<br>
├── scripts/ # Python, R, or other code scripts<br>
├── notebooks/ # Jupyter or Colab notebooks<br>
├── data/ # Datasets (CSV, XLSX, etc.)<br>
├── reports/ # Final reports (PDF, DOCX)<br>
├── documents/ # Meeting notes, planning docs, or PDFs<br>
├── templates/ # Document or data templates<br>
└── README.md # Brief description of the project and contents<br>
<br><br><br>

## How to Create a New Project Folder (with subfolders)

Use the provided Python script to automatically generate a main folder and all required subfolders:
1. generate GitHub token: Go to https://github.com/settings/tokens and create a personal access token with the following permissions(contents: read and write)
2. create .env file in same directory as below script file to save token : OIE_TOKEN=your_github_token here
3. "example_project" replace new project name in here

===================================================================================

token = os.getenv("OIE_TOKEN")<br>
g = Github(token)<br>
repo = g.get_repo("Office-of-Institutional-Effectiveness/oie-research-data")<br>
<br>
project_name = "example_project"<br>
subfolders = [<br>
    "sql/raw", "sql/cleaned", "scripts", "notebooks",<br>
    "data", "reports", "documents", "templates"<br>
]<br>
<br>
for folder in subfolders:<br>
    path = f"{project_name}/{folder}/.gitkeep"<br>
    try:<br>
        repo.create_file(<br>
                    path=path,<br>
                    message=f"Initialize folder {path}",<br>
                    content="",  <br>
                    branch="main"<br>
                )<br>
        print(f" Created: {path}")<br>
    except Exception as e:<br>
            print(f" Failed: {path} – {e}")<br>
<br>


===================================================================================
> Do not upload your `.env` file to the repository.  
> Be sure to add `.env` to your `.gitignore` to keep your token secure.
<br><br><br>


## File Upload Guidelines
When uploading a file to any subfolder, please include metadata at the top of the file (in a comment block) using the following format:

===================================================================================

-- author: [Your Full Name or GitHub ID]<br>
-- project: [Project Folder Name]<br>
-- created: YYYY-MM-DD<br>
-- description: [Brief description of the file’s purpose]<br>

...
SELECT * FROM student_success;<br>

===================================================================================
<br><br><br>


## File Naming Convention
- use lowercase with underscores  ex) kpi_completion.sql

