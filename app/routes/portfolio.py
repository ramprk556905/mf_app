from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, auth
from app.database import get_db

router = APIRouter()

def get_current_user(token: str, db: Session = Depends(get_db)):
    user_id = auth.decode_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return db.query(models.User).get(int(user_id))

@router.post("/", response_model=schemas.PortfolioOut)
def add_portfolio(
    data: schemas.PortfolioCreate,
    token: str,
    db: Session = Depends(get_db)
):
    current_user = get_current_user(token, db)
    entry = models.Portfolio(fund_name=data.fund_name, current_value=data.current_value, user_id=current_user.id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

@router.get("/", response_model=list[schemas.PortfolioOut])
def get_portfolio(token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(token, db)
    return db.query(models.Portfolio).filter(models.Portfolio.user_id == current_user.id).all()
