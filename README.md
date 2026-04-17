## 📂 Project Files

📄 **Project Report (PDF):**  
[View PDF](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/blob/main/tableforge.pdf) | 
[Download PDF](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/raw/main/tableforge.pdf)

📊 **Presentation (PPT):**  
[View PPT](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/blob/main/CodeX_pptx.pptx) | 
[Download PPT](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/raw/main/CodeX_pptx.pptx)

# TableForge

### Spreadsheet Simplicity. Database Power.

---

# About the Project

## Introduction

Data drives almost every modern application. Whether it is a student portal, an e-commerce website, a hospital management system, or a business dashboard, structured data is usually stored in databases such as SQLite, MySQL, or PostgreSQL.

While databases are powerful, using them often requires SQL knowledge, technical tools, and experience. For many users, this becomes a barrier.

On the other hand, spreadsheets are simple, visual, and beginner-friendly. Anyone can start editing rows and columns immediately—but spreadsheets lack the strength, scalability, and reliability of real databases.

**TableForge** was built to solve this gap.

It combines the ease of spreadsheets with the power of databases, allowing users to manage data visually without writing SQL queries.

---

## What Makes TableForge Different

TableForge turns database management into a cleaner and simpler experience.

### Key Advantages

- Spreadsheet-style interface for editing records
- Direct support for real databases
- No SQL required for common operations
- Fast table browsing and editing
- Live database updates
- Modern responsive user interface

Instead of dealing with commands and queries, users interact with data in a way they already understand.

---

# Core Features

## Multi-Database Support

TableForge supports multiple popular database engines:

- SQLite
- MySQL
- PostgreSQL

This gives users flexibility to work locally or with server-based databases.

---

## Smart Table Editor

The main editor provides a spreadsheet-like environment where users can:

- Edit rows and columns
- Add new records
- Modify existing values
- Create new tables
- Add columns dynamically
- Save changes directly to database

---

## Data Tools

Built-in tools improve productivity:

- Search rows quickly
- Filter by values
- Sort columns
- Inspect tables
- Manage schema visually

---

## User Experience

The interface is designed for speed and simplicity:

- Clean layouts
- Responsive design
- Easy navigation
- Minimal learning curve
- Beginner-friendly workflow

---

# Homepage

The homepage gives users a quick understanding of the product.

Users can:

- Start a new database session
- Connect an existing database
- Learn the key benefits
- Navigate quickly

The goal is to remove confusion and help users begin immediately.

---

# Database Connection Page

Connecting databases should not be difficult.

TableForge provides a guided connection flow where users can choose a database type and enter credentials easily.

Supported connection modes include:

- Local SQLite files
- MySQL server connection
- PostgreSQL server connection

The backend uses SQLAlchemy to handle secure and flexible database connectivity.

---

# Table Editor Page

This is the main workspace of TableForge.

Inside the editor, users can:

- Click cells to edit data
- Add or remove records
- Search and filter content
- Sort columns
- Save changes in real time

It delivers spreadsheet comfort with real database strength.

---

# Technology Stack

## Frontend

- Streamlit
- JavaScript
- Custom CSS

## Backend

- Python

## Database Layer

- SQLAlchemy

## Data Handling

- Pandas

## Databases

- SQLite
- MySQL
- PostgreSQL

# Project Structure

```bash
final-round-codex/
├── home.py
├── requirements.txt
├── README.md
├── backend/
│   ├── config.py
│   ├── tables.py
│   ├── utils.py
│   └── db/
│       ├── sqlite.py
│       ├── mysql.py
│       └── postgresql.py
├── pages/
│   ├── connect_database.py
│   └── table_editor.py
```

---

# How to Run

## 1. Clone Repository

```bash
git clone <repository-url>
cd final-round-codex
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Launch Application

```bash
streamlit run home.py
```

---


# Value

TableForge is highly relevant project because it solves a real and common problem:

**How can non-technical users manage databases easily?**

It demonstrates:

* Real problem solving
* Strong UI/UX thinking
* Functional backend engineering
* Database integration
* Practical market relevance



# Roles Performed by Team Members

* **Dishi Rautela** – Backend Development & UI Enhancement
* **Soniya Negi** – User Interface Design and User Experience
* **Mahee Arya** – README Editing & Updates
* **Priyanshu Bisht** – Database Connectivity & Data Integrity

---
© 2026 TableForge — Built with ❤️ by Team CodeX

