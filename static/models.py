# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Loan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    borrower: str
    amount: float
    interest: float
    weeks: int

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    loan_id: int
    week: int
    amount: float
