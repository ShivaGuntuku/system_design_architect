from pydantic import BaseModel


class ValidationIssue(BaseModel):
    severity: str
    code: str
    message: str


class ValidationResult(BaseModel):
    valid: bool
    issues: list[ValidationIssue]