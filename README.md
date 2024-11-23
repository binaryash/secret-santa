# Secret Santa Assignment Tool

A modern, web-based application to automate Secret Santa assignments among employees. Built with **FastAPI**, this tool ensures each participant gets a unique Secret Santa, adhering to configurable constraints (e.g., no self-assignment, avoiding previous year pairings).

## Features

- Upload employee lists in Excel format.
- Optional upload of previous year's assignments to avoid repetitions.
- Generate randomized, constraint-compliant Secret Santa assignments.
- Download assignments as an Excel file.
- A clean, responsive UI using Tailwind CSS.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/binaryash/secret-santa.git
   cd secret-santa
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Run the Application

1. **Start the Server**:
   ```bash
   uvicorn app:app --reload
   ```

2. **Access the Tool**:
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Project Structure

```
.
├── app.py               # Main FastAPI application
├── templates
│   └── index.html       # Tailwind-powered UI template
├── santa
│   ├── __init__.py
│   ├── secret_santa.py  # Core assignment logic
├── tests
│   ├── __init__.py
│   └── test_secret_santa.py  # Unit tests for validation
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Input File Format

### Employee File (Required)
An Excel file with the following columns:
- **Employee_Name**: Full name of the employee.
- **Employee_EmailID**: Email ID of the employee.

Example:
| Employee_Name | Employee_EmailID      |
|---------------|-----------------------|
| Alice         | alice@example.com     |
| Bob           | bob@example.com       |
| Charlie       | charlie@example.com   |

### Previous Assignments File (Optional)
An Excel file with the following columns:
- **Employee_Name**: Full name of the employee.
- **Secret_Child_Name**: Secret Santa assignment from the previous year.

Example:
| Employee_Name | Secret_Child_Name     |
|---------------|-----------------------|
| Alice         | Bob                   |
| Bob           | Charlie               |
| Charlie       | Alice                 |

---

## Running Tests

To ensure the tool works as expected, run the provided unit tests:

```bash
pytest tests
```

---

## Known Issues and Limitations

- The tool currently supports `.xlsx` files only.
- Circular constraints may cause assignment failures (e.g., a single participant).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

