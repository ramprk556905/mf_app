from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, funds, portfolio

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mutual Fund Backend")

app.include_router(users.router, prefix="/auth", tags=["Auth"])
app.include_router(funds.router, prefix="/funds", tags=["Funds"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])

@app.get("/")
def root():
    return {"message": "Welcome to Mutual Fund Backend"}