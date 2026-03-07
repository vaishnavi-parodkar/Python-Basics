# 🐍 Python-Basics

A structured, hands-on Python learning repository covering everything from core fundamentals to real-world programs — organized progressively for learners at any stage.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📁 Repository Structure

```
Python-Basics/
├── Basics/                         # Core Python concepts
│   ├── 1-virtual-environment       # Setting up virtual environments
│   ├── 2-Anaconda                  # Anaconda setup & usage
│   ├── 3-Packages-and-pip          # Package management
│   ├── 4-interactive-python        # Interactive Python (REPL)
│   ├── 5-variables                 # Variables & naming conventions
│   ├── 6-Data-types                # Python data types
│   ├── 7-Operators                 # Arithmetic, logical, comparison operators
│   ├── 8-Lists                     # Lists & list methods
│   ├── 9-Tuples                    # Tuples & immutability
│   ├── 10-Dictionaries             # Dictionaries & key-value pairs
│   └── 11-Sets                     # Sets & set operations
│
├── Building Programs/              # Intermediate programming concepts
│   ├── 1-Functions.txt             # Defining & using functions
│   ├── 2-External-Tools.txt        # Working with external libraries
│   ├── 3-Practical-Python.txt      # Real-world Python patterns
│   ├── 4-Error-Handling.txt        # Exceptions & error handling
│   └── 5-Classes.txt               # OOP & class definitions
│
├── Tools/                          # Developer tooling & best practices
│   ├── Environment-and-secrets.txt # Managing env variables & secrets
│   └── Modern-Python.txt           # Modern Python features & idioms
│
├── data/                           # Sample datasets
│   └── paris_weather.csv           # Weather data for practice
│
├── sales-analysis/                 # Real-world data analysis project
│   ├── data/
│   │   └── sales.csv               # Raw sales data
│   ├── output/
│   │   ├── sales_data.json         # Processed output (JSON)
│   │   ├── sales_data.xlsx         # Processed output (Excel)
│   │   └── sales_with_totals.csv   # Enriched CSV with totals
│   ├── analyzer.py                 # Core analysis logic
│   └── helpers.py                  # Utility/helper functions
│
├── BFS.py                          # Breadth-First Search implementation
├── DFS.py                          # Depth-First Search implementation
├── bestFirstSearch.py              # Best-First Search algorithm
├── Basics.py                       # General basics script
├── Build-Programs.py               # Program-building exercises
├── RealWorldClassesEx.py           # Real-world OOP examples
├── classes.py                      # Class definitions & practice
└── README.md
```

---

## 🌟 What's Covered

| Topic | Description |
|---|---|
| **Environment Setup** | Virtual environments, Anaconda, pip, packages |
| **Python Fundamentals** | Variables, data types, operators, collections |
| **Data Structures** | Lists, tuples, dictionaries, sets |
| **Functions** | Defining, calling, and organizing functions |
| **OOP** | Classes, objects, real-world examples |
| **Error Handling** | Try/except, custom exceptions |
| **Algorithms** | BFS, DFS, Best-First Search |
| **Data Analysis** | CSV/JSON/Excel processing with real sales data |
| **Modern Python** | Best practices, tooling, secrets management |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ installed → [Download](https://www.python.org/downloads/)
- `pip` for package management (comes with Python)
- Optionally, [Anaconda](https://www.anaconda.com/) for environment management

### Clone the Repository

```bash
git clone https://github.com/vaishnavi-parodkar/Python-Basics.git
cd Python-Basics
```

### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### Run Any Script

```bash
python BFS.py
python classes.py
python sales-analysis/analyzer.py
```

---

## 📊 Sales Analysis Project

The `sales-analysis/` folder is a mini real-world project demonstrating:

- Reading raw CSV data
- Processing and computing totals
- Exporting results to **JSON**, **Excel (.xlsx)**, and **enriched CSV**
- Separating logic into `analyzer.py` and helper utilities in `helpers.py`

```bash
cd sales-analysis
python analyzer.py
```

Outputs will be saved in the `output/` folder.

---

## 🔍 Algorithm Implementations

Three classic search algorithms implemented as standalone scripts:

| File | Algorithm | Use Case |
|---|---|---|
| `BFS.py` | Breadth-First Search | Shortest path in unweighted graphs |
| `DFS.py` | Depth-First Search | Exploring all paths, cycle detection |
| `bestFirstSearch.py` | Best-First Search | Heuristic-guided traversal |

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Standard Library** — `csv`, `json`, `os`, `collections`
- **openpyxl** — for Excel file generation
- **Git & GitHub** — version control

---

## 📬 Contact

For questions, suggestions, or collaborations:

- 📧 **Email:** vaishnaviparodkar@gmail.com
- 🐙 **GitHub:** [@vaishnavi-parodkar](https://github.com/vaishnavi-parodkar)

