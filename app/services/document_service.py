# app/services/document_service.py
from app.models.document_model import RequestBody, ResponseBody, get_current_timestamp
from pydantic import ValidationError
from bson import ObjectId


def validate_document(request_data: dict) -> tuple:
    try:
        request = RequestBody(**request_data)
        document_id = str(request._id or ObjectId())

        response = ResponseBody(
            _id=document_id,
            status="valid",
            validation_errors=[],
            processed_at=get_current_timestamp()
        )
        return response.dict(), 200

    except ValidationError as e:
        errors = [error["msg"] for error in e.errors()]
        document_id = str(ObjectId())  # fallback if _id validation failed
        response = ResponseBody(
            _id=document_id,
            status="invalid",
            validation_errors=errors,
            processed_at=get_current_timestamp()
        )
        return response.dict(), 422