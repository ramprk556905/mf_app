# Mutual Fund Backend

A FastAPI-based backend app for a mutual fund broker.

## Features

- Register/Login users
- Add/View portfolio
- Integrate with RapidAPI for open-ended schemes
- E2E test with pytest

## Getting Started

```bash
git clone https://github.com/ramprk556905/mf_app.git
cd bhive-backend
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload


to run the test_e2e.py use below command
PYTHONPATH=. pytest tests
