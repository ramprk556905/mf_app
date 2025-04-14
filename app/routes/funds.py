from fastapi import APIRouter, Depends
import httpx, os
from app.schemas import FundRequest

router = APIRouter()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

@router.post("/schemes/")
async def get_funds(data: FundRequest):
    """
    Fetch mutual fund schemes based on the provided fund family.
    Sends a GET request to an external API with the specified parameters.
    Returns the JSON response from the external API.
    """
    url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchSchemes"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "latest-mutual-fund-nav.p.rapidapi.com"
    }
    params = {"Category": "Open Ended Schemes", "FundFamily": data.fund_family}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        return response.json()
