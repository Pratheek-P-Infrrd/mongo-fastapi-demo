from fastapi import APIRouter, HTTPException
from app.models.document_model import DocumentModel
from app.services.document_service import validate_document

router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"]
)

@router.post("/validate")
async def validate_document_api(document: DocumentModel):
    try:
        result = validate_document(document)
        if result["status"] == "invalid":
            return {"status": "invalid", **result}
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
