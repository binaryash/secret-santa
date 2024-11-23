# **Secret Santa Assignment Tool Documentation**

## Overview

The **Secret Santa Assignment Tool** is a web application built using FastAPI to automate the Secret Santa process for organizations. It ensures that all participants are assigned a Secret Santa while adhering to specific constraints, such as avoiding self-assignment and ensuring no repeated assignments from previous years.

---

## Features

- **File Uploads**: Accepts employee lists and optional previous year's assignments in Excel format.
- **Constraint Handling**:
  - No self-assignment.
  - Avoids repeated assignments based on previous year data.
- **Randomized Assignments**: Generates assignments ensuring fairness.
- **Output Generation**: Provides the results in an Excel file.
- **Responsive UI**: Tailwind CSS-powered modern and user-friendly interface.

---

## System Requirements

- **Python Version**: 3.9 or higher
- **Dependencies**: Listed in `requirements.txt` (e.g., FastAPI, pandas, openpyxl, etc.).

---

## Installation Guide

### Prerequisites

Ensure you have the following installed:
- Python (3.9 or higher)
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/binary-ash/secret-santa.git
   cd secret-santa
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Application**:
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## File Specifications

### **Employee List (Required)**

Upload an Excel file containing the following columns:

| **Column**        | **Description**                          |
|--------------------|------------------------------------------|
| `Employee_Name`    | Full name of the employee.              |
| `Employee_EmailID` | Email address of the employee.          |

#### Example:
| Employee_Name | Employee_EmailID      |
|---------------|-----------------------|
| Alice         | alice@example.com     |
| Bob           | bob@example.com       |
| Charlie       | charlie@example.com   |

---

### **Previous Assignments (Optional)**

Upload an Excel file containing the following columns:

| **Column**           | **Description**                          |
|-----------------------|------------------------------------------|
| `Employee_Name`       | Full name of the employee.              |
| `Secret_Child_Name`   | Name of the employee's assigned Santa.  |

#### Example:
| Employee_Name | Secret_Child_Name     |
|---------------|-----------------------|
| Alice         | Bob                   |
| Bob           | Charlie               |
| Charlie       | Alice                 |

---

## Application Workflow

1. **Upload Files**:
   - Employee list (required).
   - Previous assignments (optional).

2. **Processing**:
   - Validates the uploaded files.
   - Randomly assigns Secret Santas while ensuring constraints:
     - No self-assignment.
     - No repeated assignments (if previous year file is uploaded).

3. **Output**:
   - Generates an Excel file containing the assignments.

---

## Output File

The output Excel file contains the following columns:

| **Column**             | **Description**                            |
|-------------------------|--------------------------------------------|
| `Employee_Name`         | Name of the employee.                     |
| `Employee_EmailID`      | Email address of the employee.            |
| `Secret_Child_Name`     | Name of the assigned Secret Santa child.  |
| `Secret_Child_EmailID`  | Email address of the Secret Santa child.  |

---

## Testing the Application

### Running Tests

The project includes unit tests to validate the core logic. To run the tests:
```bash
pytest tests
```

### Key Tests

1. **Valid Assignments**:
   - Ensures each employee is assigned a valid Secret Santa.

2. **Constraint Handling**:
   - Ensures no self-assignment and avoids repeats from the previous year.

3. **Error Handling**:
   - Validates appropriate errors are raised for invalid input files.

---

## Error Handling

The application provides clear error messages for the following scenarios:
1. **Missing Columns**:
   - If required columns (`Employee_Name`, `Employee_EmailID`) are not present in the uploaded file.
2. **No Valid Assignments**:
   - When constraints prevent valid Secret Santa assignments.
3. **Unsupported File Types**:
   - If non-Excel files are uploaded.

---

## Project Structure

```
.
├── app.py               # Main FastAPI application
├── templates/
│   └── index.html       # Tailwind-powered UI template
├── santa/
│   ├── __init__.py
│   ├── secret_santa.py  # Core logic for assignments
├── tests/
│   ├── __init__.py
│   └── test_secret_santa.py  # Unit tests for functionality
├── docs/
│   └── docs.md          # Full documentation
├── requirements.txt     # Python dependencies
└── README.md            # Basic overview
```

---

## Common Issues

1. **Circular Constraints**:
   - The tool may fail if the constraints (e.g., avoiding repeats) make assignments impossible. This will raise an error: 
     ```
     RuntimeError: No valid assignment for <Employee_Name>.
     ```

2. **Invalid File Format**:
   - Ensure files are in `.xlsx` format. Other file types (e.g., CSV) are not supported.

---

## Roadmap

Planned features for future updates:
- Support for additional file formats (e.g., CSV).
- Enhanced error reporting and logs.
- User authentication for secure access.
- API endpoints for integration with third-party tools.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.
