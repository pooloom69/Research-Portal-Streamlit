OIE Query Vault
Secure Research File Access Portal
🔍 Overview

The OIE Research App is a secure, web-based internal tool developed for the Office of Institutional Effectiveness at a California community college. It enables staff to efficiently access, filter, and download research project files and metadata through an intuitive Streamlit interface.

The platform is designed to centralize research data access, streamline project tracking, and maintain institutional data security through Azure integration.

⚙️ Tech Stack

Frontend: Streamlit (Python)

Backend: Python

Hosting: Azure App Service

CI/CD: Azure DevOps Pipelines

Authentication: Microsoft Identity Platform (Azure AD)

🧩 Key Features

Secure Login – Microsoft account authentication ensures role-based access control.

Smart Search & Filter – Browse research documents by category, status, or date.

Metadata View – Display file owner, author, and last updated date.

File Preview & Download – Safely preview or download selected research materials.

Automated CI/CD – Streamlined deployment via Azure DevOps for continuous updates.

<img width="783" height="342" alt="Screenshot 2025-11-10 at 9 03 34 AM" src="https://github.com/user-attachments/assets/636979d1-4abb-4638-bc78-787c79b33812" />


🎯 Purpose

This app was created to modernize internal workflows by:

Reducing manual file retrieval and sharing.

Improving transparency and consistency in data research projects.

Enhancing data governance with Azure-based access management.

👥 Target Users

Staff members of the Office of Institutional Effectiveness (OIE) who handle institutional data research, documentation, and project requests.

🚀 Deployment Workflow

Commit code to main branch in Azure Repos or GitHub.

CI/CD pipeline automatically builds and deploys updates to Azure App Service.

Authentication and user access managed via Azure Active Directory (AAD).
