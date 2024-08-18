from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from app.pdf.template1 import TemplateCv1
from app.api.models import CVData
import io
import os
import shutil

router = APIRouter()

@router.post("/pdf")
async def generate_cv(data: CVData):
    try:
        # Create a BytesIO buffer
        buffer = io.BytesIO()

        # Create an instance of TemplateCv1 with the buffer
        cv_creator = TemplateCv1(buffer)

        # Build the PDF with the provided data
        cv_creator.build_pdf(data.dict())

        # Seek to the beginning of the buffer
        buffer.seek(0)

        # Create a filename
        filename = f"cv_{data.name.replace(' ', '_')}.pdf"

        # Return the document as a response
        return StreamingResponse(
            buffer,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    except Exception as e:
        print(f"Error generating CV: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail="Error generating CV")

@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    try:
        # Create the directory if it doesn't exist
        upload_dir = "app/api/pdf_uploaded"
        os.makedirs(upload_dir, exist_ok=True)

        # Create the file path
        file_path = os.path.join(upload_dir, file.filename)

        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={"message": "CV uploaded successfully", "filename": file.filename}, status_code=200)
    except Exception as e:
        print(f"Error uploading CV: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail="Error uploading CV")
