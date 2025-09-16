# app/models/document_model.py
from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
from typing import List, Optional
from bson import ObjectId


# Pydantic-compatible ObjectId wrapper
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class RequestBody(BaseModel):
    _id: Optional[PyObjectId] = None
    document_type: str
    borrower_name: str
    employer_name: str
    pay_period_start: date
    pay_period_end: date
    gross_income: float

    @field_validator("pay_period_start", "pay_period_end", mode="before")
    def validate_date_format(cls, v):
        if isinstance(v, str):
            try:
                # Try parsing full datetime first
                dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
                return dt.date()
            except ValueError:
                try:
                    # Fallback to plain date
                    return date.fromisoformat(v)
                except ValueError:
                    raise ValueError("Invalid date format, must be 'YYYY-MM-DD' or full ISO datetime")
        if isinstance(v, date):
            return v
        raise ValueError("Invalid type for date field")

    @field_validator("gross_income")
    def validate_gross_income(cls, v):
        if v <= 0:
            raise ValueError("Gross income must be a positive number")
        return v

    @field_validator("document_type", "borrower_name", "employer_name")
    def validate_non_empty_fields(cls, v, info):
        if not v.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return v
    
    @field_validator("pay_period_end")
    def check_dates(cls, v, values):
        start = values.data.get("pay_period_start")
        if start and v < start:
            raise ValueError("pay_period_end must be after pay_period_start")
        return v


class ResponseBody(BaseModel):
    _id: str
    status: str
    validation_errors: List[str]
    processed_at: str


def get_current_timestamp() -> str:
    """ Get the current UTC timestamp in ISO format """
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
