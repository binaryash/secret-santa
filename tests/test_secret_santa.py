
import pandas as pd
import pytest
from santa.secret_santa import SecretSanta


def test_valid_assignments():
    """
    Test: Validate the basic functionality of Secret Santa assignments.
    - Ensures all employees are assigned a unique Secret Santa.
    - Checks that assignments cover all employees and are valid.
    """
    employees_data = {
        "Employee_Name": ["Alice", "Bob", "Charlie"],
        "Employee_EmailID": ["alice@example.com", "bob@example.com", "charlie@example.com"]
    }
    employees_df = pd.DataFrame(employees_data)

    santa = SecretSanta(employees_df)
    assignments_df = santa.generate_assignments()

    # Ensure assignments are not empty and all employees are covered
    assert not assignments_df.empty
    assert len(assignments_df) == len(employees_df)

    # Validate assigned names and ensure all are valid
    assert set(assignments_df["Employee_Name"]) == set(employees_df["Employee_Name"])
    assert set(assignments_df["Secret_Child_Name"]).issubset(set(employees_df["Employee_Name"]))


def test_previous_assignments_constraint():
    """
    Test: Ensure employees are not assigned the same Secret Santa as in the previous year.
    - Validates constraint against repeating assignments.
    """
    employees_data = {
        "Employee_Name": ["Alice", "Bob", "Charlie"],
        "Employee_EmailID": ["alice@example.com", "bob@example.com", "charlie@example.com"]
    }
    employees_df = pd.DataFrame(employees_data)

    previous_data = {
        "Employee_Name": ["Alice", "Bob", "Charlie"],
        "Secret_Child_Name": ["Bob", "Charlie", "Alice"]
    }
    previous_df = pd.DataFrame(previous_data)

    santa = SecretSanta(employees_df, previous_df)
    assignments_df = santa.generate_assignments()

    # Ensure all employees are covered
    assert not assignments_df.empty
    assert len(assignments_df) == len(employees_df)

    # Validate no employee gets the same Secret Santa as in the previous year
    for _, row in assignments_df.iterrows():
        previous_child = previous_df[previous_df["Employee_Name"] == row["Employee_Name"]]["Secret_Child_Name"].values
        assert row["Secret_Child_Name"] not in previous_child


def test_invalid_employee_file():
    """
    Test: Ensure the program raises a validation error for an invalid employee file.
    - Verifies the absence of required columns results in a ValueError.
    """
    employees_data = {
        "Wrong_Column1": ["Alice", "Bob", "Charlie"],
        "Wrong_Column2": ["alice@example.com", "bob@example.com", "charlie@example.com"]
    }
    employees_df = pd.DataFrame(employees_data)

    with pytest.raises(ValueError, match="Employee file must contain these columns"):
        santa = SecretSanta(employees_df)
        santa.generate_assignments()


def test_no_possible_assignments():
    """
    Test: Ensure the program handles cases where no valid assignments are possible.
    - Example: A single employee where self-assignment is not allowed.
    """
    employees_data = {
        "Employee_Name": ["Alice"],
        "Employee_EmailID": ["alice@example.com"]
    }
    employees_df = pd.DataFrame(employees_data)

    with pytest.raises(RuntimeError, match="Could not assign a secret child"):
        santa = SecretSanta(employees_df)
        santa.generate_assignments()

