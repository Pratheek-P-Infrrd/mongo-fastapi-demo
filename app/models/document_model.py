from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Optional

class DocumentModel(BaseModel):
    document_type: str = Field(..., min_length=1)
    borrower_name: str = Field(..., min_length=1)
    employer_name: str = Field(..., min_length=1)
    pay_period_start: date
    pay_period_end: date
    gross_income: float = Field(..., gt=0)

    @field_validator("pay_period_end")
    def validate_end_after_start(cls, v, info):
        start = info.data.get("pay_period_start")
        if start and v < start:
            raise ValueError("pay_period_end must be after pay_period_start")
        return v
