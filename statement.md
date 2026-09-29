# Employee Management System — Project Statement

## Problem Statement
Small to medium-sized organizations often struggle to manage employee records without resorting to overly complex, expensive enterprise software. Relying on disorganized spreadsheets leads to data entry errors, accidental deletions, and a lack of structured data validation. Organizations need a **lightweight, terminal-based database system** that allows administrators to dynamically add, remove, look up, and update employee attributes (like experience, salary, and active status) without operational friction.

## Scope of the Project
This project consists of a multi-module Python application that provides a Command Line Interface (CLI) for managing a local, list-based employee database in real-time.

### In-Scope
* **Core CRUD Operations:** Features to dynamically add data, remove records by ID, view individual profiles, and print full database logs.
* **Granular Field Modification:** Dedicated sub-menus to update specific columns including Employee ID, Name, Experience, Salary, Date of Joining, and Employment Status.
* **Business Logic Operations:** A specialized feature to increase an employee's salary by a specific flat rate.
* **Input Validation:** Error handling using `try-except` blocks to catch data type mismatches (e.g., preventing text inputs where integers like IDs or salaries are required).

### Out-of-Scope
* Permanent data storage (persistent databases like SQLite, MySQL, or saving data to external `.csv`/`.json` files).
* Graphical User Interface (GUI) or web application access.
* Advanced payroll calculators (tax deductions, bonuses, or hourly tracking).

## Target Users
* **HR Administrators / Operations Managers:** Who need a straightforward tool to onboard new employees, change worker status, and track historical start dates.
* **Small Business Owners:** Who need a rapid, zero-overhead utility to review staff lists, adjust compensation packages, and track years of experience.

## High-Level Features
* **Modular Code Architecture:** Separates code into logical layers: a master loop control (`main.py`), a table modification handler (`modify.py`), and atomic operational scripts (`function_of_main_projects.py` and `function_of_modify.py`).
* **Interactive CLI Menu:** A continuous loop menu that guides users step-by-step using numeric input selections.
* **Dynamic Record Mutation:** Built-in table filtering that scans rows by Employee ID to securely update details or remove elements inline.
* **Robust Exception Safety:** Recursively restarts operational inputs if an administrator enters invalid formats, ensuring the script does not crash unexpectedly.
