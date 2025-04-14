from pydantic import BaseModel, EmailStr,ConfigDict
from typing import List

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class FundRequest(BaseModel):
    fund_family: str

class PortfolioOut(BaseModel):
    fund_name: str
    current_value: float

class PortfolioCreate(BaseModel):
    fund_name: str
    current_value: float
