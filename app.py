
from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import io
from santa.secret_santa import SecretSanta

# Initialize FastAPI app and set up templates directory
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    """
    Renders the main page with the form for uploading employee and previous year files.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/assign")
async def assign_santa(employee_file: UploadFile, previous_file: UploadFile = None):
    """
    Handles the Secret Santa assignment logic:
    - Processes the employee and previous year files.
    - Generates valid assignments based on constraints.
    - Returns an Excel file with the assignments.
    """
    try:
        # Read and parse the employee file into a DataFrame
        employees_df = pd.read_excel(io.BytesIO(await employee_file.read()))

        # Read and parse the optional previous year file if provided
        previous_df = None
        if previous_file:
            previous_df = pd.read_excel(io.BytesIO(await previous_file.read()))

        # Generate Secret Santa assignments
        santa = SecretSanta(employees_df, previous_df)
        assignments_df = santa.generate_assignments()

        # Save assignments to an Excel file and return it as a response
        output_path = "Secret_Santa_Assignments.xlsx"
        assignments_df.to_excel(output_path, index=False)
        return FileResponse(output_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="Secret_Santa_Assignments.xlsx")
    
    # Handle validation errors (e.g., missing columns in input files)
    except ValueError as e:
        return {"error": f"Validation error: {str(e)}"}
    
    # Handle logical errors during assignment generation
    except RuntimeError as e:
        return {"error": f"Assignment error: {str(e)}"}
    
    # Handle unexpected errors
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

