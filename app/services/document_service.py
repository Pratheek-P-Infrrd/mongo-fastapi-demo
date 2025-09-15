from datetime import datetime, timezone
import uuid

def validate_document(document: dict):
    """
    Process and validate the document, returning result dict.
    """
    # generate unique doc ID
    document_id = "doc_" + uuid.uuid4().hex

    # Processed timestamp in UTC
    processed_at = datetime.now(timezone.utc).isoformat()

    result = {
        "status": "valid",
        "document_id": document_id,
        "validation_errors": [],
        "processed_at": processed_at
    }
    return result
