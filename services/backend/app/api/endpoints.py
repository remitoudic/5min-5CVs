from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
# from app.pdf.template1 import TemplateCv1
from app.pdf.template3 import TemplateCv3
from app.api.models import CVData
import io

router = APIRouter()


@router.post("/pdf")
async def generate_cv(data: CVData):
    try:
        # Create a BytesIO buffer
        buffer = io.BytesIO()

        # Create an instance of template
        # cv_creator = TemplateCv1(buffer)
        cv_creator = TemplateCv3(buffer)
        # Build the PDF
        cv_creator.build_pdf(data.model_dump())

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
