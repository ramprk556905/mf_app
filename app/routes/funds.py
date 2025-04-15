from fastapi import APIRouter,HTTPException
import httpx, os
from app.schemas import FundRequest

router = APIRouter()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

@router.post("/schemes")
async def get_funds(data: FundRequest):
    """
    Fetch mutual fund schemes based on the scheme type provided by the user.
    Sends a GET request to the external RapidAPI Mutual Fund endpoint.
    """
    url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com"
    }
    params = {
        "Scheme_Type": data.scheme_type 
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))