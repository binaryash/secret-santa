
import pandas as pd
import random
from typing import Optional


class SecretSanta:
    """
    Handles Secret Santa assignments with validation and constraints.
    """
    def __init__(self, employees_df: pd.DataFrame, previous_df: Optional[pd.DataFrame] = None):
        self.employees_df = employees_df
        self.previous_df = previous_df

    def validate_employees(self):
        # Ensure employee file contains required columns
        if not {"Employee_Name", "Employee_EmailID"}.issubset(self.employees_df.columns):
            raise ValueError("Employee file must contain 'Employee_Name' and 'Employee_EmailID'.")

    def validate_previous_assignments(self):
        # Ensure previous assignments file (if provided) contains required columns
        if self.previous_df is not None:
            if not {"Employee_Name", "Secret_Child_Name"}.issubset(self.previous_df.columns):
                raise ValueError("Previous file must contain 'Employee_Name' and 'Secret_Child_Name'.")

    def generate_assignments(self) -> pd.DataFrame:
        # Validate input files
        self.validate_employees()
        if self.previous_df is not None:
            self.validate_previous_assignments()

        # Prepare assignment data
        employees = list(self.employees_df["Employee_Name"])
        emails = list(self.employees_df["Employee_EmailID"])
        available = employees[:]
        assignments = []

        for employee in employees:
            # Exclude self and previous year's assignments
            possible = [child for child in available if child != employee]
            if self.previous_df is not None:
                prev = self.previous_df[self.previous_df["Employee_Name"] == employee]["Secret_Child_Name"].tolist()
                possible = [child for child in possible if child not in prev]

            if not possible:
                raise RuntimeError(f"No valid assignment for {employee}. Check constraints.")

            # Randomly assign and update
            child = random.choice(possible)
            available.remove(child)
            assignments.append({
                "Employee_Name": employee,
                "Employee_EmailID": emails[employees.index(employee)],
                "Secret_Child_Name": child,
                "Secret_Child_EmailID": emails[employees.index(child)]
            })

        return pd.DataFrame(assignments)

