from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import pandas as pd
import shutil
import uvicorn
from typing import Literal
import os

app = FastAPI()

@app.post("/upload-and-process/")
def upload_and_process(file: UploadFile = File(...), file_type: Literal["csv", "xlsx"] = "xlsx"):
    # Save uploaded file
    uploaded_path = f"input_file.{file_type}"
    with open(uploaded_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run automation (you'll refactor web_aut.py into a function)
    from web_aut import run_automation  # this should return path of the updated file + row count
    updated_file_path, row_count = run_automation(uploaded_path)

    return {
        "processed_rows": row_count,
        "updated_file": updated_file_path
    }

@app.get("/download/")
def download_file():
    return FileResponse("Updated.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="Updated.xlsx")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8889)
