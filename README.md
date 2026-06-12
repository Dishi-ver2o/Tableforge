## 📂 Project Files

📊 **Presentation (PPT):**
[View PPT](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/blob/main/CodeX_pptx.pptx) | [Download PPT](https://github.com/WTC-Group-2/wtc-round-2-group-2-codex/raw/main/CodeX_pptx.pptx)

---

# TableForge

### Spreadsheet Simplicity. Database Power.

---

## Introduction

Data is everywhere today. Nearly every modern application depends on databases to store, organize, and manage information. Popular systems such as SQLite, MySQL, and PostgreSQL power everything from student portals and e-commerce platforms to enterprise dashboards.

However, working with databases is often difficult for non-technical users. Traditional tools usually require:

* SQL knowledge
* Complex setup processes
* Technical understanding of schemas and queries
* Developer-focused interfaces

At the same time, spreadsheet tools are simple and familiar—but they lack the scalability, structure, and reliability of real databases.

**TableForge was built to bridge this gap.**

It combines the comfort of spreadsheets with the strength of databases, allowing users to manage structured data visually without needing to write SQL.

---

## What Makes TableForge Different

TableForge transforms database management into a practical and user-friendly experience.

### Key Advantages

* Spreadsheet-style editing interface
* Real database connectivity
* No SQL required for everyday operations
* Search, sort, and filtering tools
* Live updates to connected databases
* Dynamic table creation and column management
* Support for multiple database systems
* Clean modern interface built for productivity

Instead of commands and complicated panels, users interact directly with data in a familiar grid-based workspace.

---

## Why TableForge Matters

Many database platforms are built primarily for developers and administrators. This creates friction for:

* Students
* Beginners
* Office teams
* Small businesses
* Analysts
* Non-technical users

TableForge removes unnecessary complexity while preserving the real power of relational databases.

It gives users full control over their data through a simpler and more approachable interface.

---

# Core Features

## Multi-Database Support

TableForge supports multiple database engines such as:

* SQLite
* MySQL
* PostgreSQL

This allows users to work locally or connect to production-ready server databases.

---

## Smart Table Editor

The main editor provides a spreadsheet-like experience where users can:

* Edit rows and columns visually
* Add new records
* Modify existing data
* Create new tables
* Add columns dynamically
* Save changes directly to the connected database

---

## Data Tools

Built-in tools improve speed and workflow:

* Search rows instantly
* Filter records by value
* Sort columns
* Inspect available tables
* Manage schema visually

---

## User Experience

The interface is designed for simplicity and speed:

* Clean layouts
* Responsive design
* Easy navigation
* Minimal learning curve
* Beginner-friendly workflow

---

## Homepage

The homepage is designed to make users comfortable immediately.

It provides clear options to:

* Start a new session
* Connect an existing database
* Understand the product quickly
* Navigate with ease

The goal is fast onboarding with zero confusion.

---

## Database Connection Page

Connecting a database should be simple.

TableForge offers a guided connection flow where users can choose their database type and connect securely.

Supported connection modes include:

* Local SQLite files
* MySQL server connection
* PostgreSQL server connection

The backend uses SQLAlchemy for stable and flexible database connectivity.

---

## Table Editor Page

This is the core workspace of TableForge.

Inside the editor, users can:

* Click cells to edit data
* Add or remove rows
* Search and filter content
* Sort columns
* Manage tables visually
* Save changes in real time

It combines spreadsheet familiarity with database reliability.

---

# Technology Stack

* **Frontend** — Streamlit, JavaScript, Custom CSS

* **Backend** — Python

* **Database Layer** — SQLAlchemy

* **Data Handling** — Pandas

* **Databases** — SQLite, MySQL, PostgreSQL

---

# Project Structure

```bash id="6vqg34"
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

```bash id="9uddb3"
git clone <repository-url>
cd final-round-codex
```

## 2. Install Dependencies

```bash id="kdrzjk"
pip install -r requirements.txt
```

## 3. Launch Application

```bash id="yzt0rj"
streamlit run home.py
```

---

# Project Value

TableForge solves a common real-world problem:

**How can non-technical users manage databases easily without learning SQL?**

It demonstrates:

* Real problem solving
* Strong UI/UX thinking
* Functional backend engineering
* Multi-database integration
* Practical usability
* Product potential beyond hackathons

---

---

© 2026 TableForge — Built with ❤️ by Priyanshu
