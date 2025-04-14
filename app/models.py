from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    """
    Represents a user in the system.
    Stores user details such as email and hashed password.
    Establishes a relationship with the Portfolio table.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    portfolio = relationship("Portfolio", back_populates="owner")

class Portfolio(Base):
    """
    Represents a portfolio entry for a user.
    Stores details such as fund name, current value, and associated user ID.
    Establishes a relationship with the User table.
    """
    __tablename__ = "portfolios"
    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String)
    current_value = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="portfolio")