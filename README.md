
# Employee Database Management System

A modular, terminal-based database application written in Python. This system allows organizations to manage employee records dynamically through a Command-Line Interface (CLI). It supports core CRUD capabilities—allowing users to add records, remove entries, query specific records, display all database contents, and perform structural modifications on individual fields (IDs, names, experience, and salaries).

Developed by: **Priyesh Patidar**

---

## 📂 Project Architecture

The application is structured into four distinct Python modules to separate concerns and handle code maintenance:

* **`main.py`** – The application entrance point. Contains the main execution loop, handles parent-level menu options, and checks loop continuity.
* **`function_of_main_projects.py`** – Contains fundamental database actions including adding, removing, viewing, and printing data records.
* **`modify.py`** – Manages the structural modifications submenu allowing users to select which attributes they intend to update.
* **`function_of_modify.py`** – Contains the low-level processing logic to isolate and re-assign specific employee field variables (IDs, Names, Experience, Salaries).

---

## 🚀 Prerequisites

Before running this project, verify you have the following installed on your machine:
* **Python 3.14** 

Verify your current environment installation by typing this command into your terminal:
```bash
python --version 3.14
---

## 🛠️ Setup & Local Installation

Follow these steps exactly to pull down and run the workspace from your terminal:

### 1. Clone the Public Repository
Download the source files using git:
```bash
git clone https://github.com/priyeshpatidar/priyesh_vit_bhopal
```

### 2. Move Into the Project Root
Shift your directory path into the folder containing the downloaded code files:
```bash
cd priyesh_vit_bhopal
```

### 3. File Verification & Naming Setup
To ensure the multi-file module imports execute properly without throwing `ModuleNotFoundError` anomalies, name your files exactly as follows in your working directory:
1. Save the main program as `main.py`
2. Save the primary data actions file as `function_of_main_projects.py`
3. Save the main modify logic file as `modify.py`
4. Save the secondary modify operations file as `function_of_modify.py`

*No external dependencies or third-party packages need to be installed via `pip`.*

---

## 💻 Execution & Usage

The project is fully executable via the command-line terminal environment and has zero GUI dependencies.

### Launching the Application
Execute the primary script file inside your terminal window to open the interactive database shell:
```bash
python main.py
```

### Navigating the Interface Menus

#### 1. The Main Menu
When launched, you can choose from these options by entering the respective numeric key:
* **`1` - Add Data:** Prompts you for the total number of logs to add, then collects the `ID`, `Name`, `Experience`, and `Salary` for each.
* **`2` - Remove Data:** Safely drops a row entry match based on the provided employee ID.
* **`3` - Show Specific Data:** Queries the system for a matching `emp_id` and prints that single employee's array.
* **`4` - Show All Data:** Loops through and displays all rows inside the application memory.
* **`5` - Modify Data:** Branches off into the configuration adjustment submenu.

#### 2. The Modification Submenu
Selecting Option `5` routes your application terminal path into a specialized attribute editor:
* **`1`** – Alters the employee's designated identification index value (`ID`).
* **`2`** – Updates the string characters forming the employee's stored `Name`.
* **`3`** – Edits numerical data tracking total years of field `Experience`.
* **`4`** – Overwrites data elements representing active financial tracking allocations (`Salary`).

#### 3. Session Control
After every choice, the program asks: `do you want to continue(y/n)`. Type `y` to return to the main dashboard menu, or `n` to break the terminal execution cycle safely.

# by priyesh patidar
