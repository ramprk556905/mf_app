from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List

class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    Includes fields for email and password.
    Used for user registration requests.
    """
    email: EmailStr
    password: str

class Token(BaseModel):
    """
    Schema for representing an authentication token.
    Includes the access token and its type.
    Used for login responses.
    """
    access_token: str
    token_type: str

class UserOut(BaseModel):
    """
    Schema for returning user details.
    Includes the user ID and email.
    Used for responses after user registration.
    """
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class FundRequest(BaseModel):
    """
    Schema for requesting mutual fund data.
    Includes the fund family as a parameter.
    Used for fetching fund schemes.
    """
    scheme_type: str

class PortfolioOut(BaseModel):
    """
    Schema for returning portfolio details.
    Includes the fund name and its current value.
    Used for portfolio retrieval responses.
    """
    fund_name: str
    current_value: float

class PortfolioCreate(BaseModel):
    """
    Schema for creating a new portfolio entry.
    Includes the fund name and its current value.
    Used for portfolio creation requests.
    """
    fund_name: str
    current_value: float
