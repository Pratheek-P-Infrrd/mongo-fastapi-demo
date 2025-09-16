# app/routes/document_routes.py
from fastapi import APIRouter, HTTPException
from app.services.document_service import validate_document
from typing import Dict

router = APIRouter(prefix="/api/v1/documents", tags=["Documents"])


@router.post("/validate")
async def validate_document_route(request_data: Dict):
    """
    Route to validate a document.
    """
    response, status_code = validate_document(request_data)

    if status_code == 200:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response)

