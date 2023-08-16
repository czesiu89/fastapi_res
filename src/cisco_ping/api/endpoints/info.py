from typing import Dict
from fastapi import APIRouter

prefix = "/info"
router = APIRouter(prefix=prefix)


@router.get("/", include_in_schema=False)
@router.get("", description="Print the info endpoint")
def info() -> Dict:
    """
    GET - info
    response: 200 OK
    """
    return {"Receiver": "Cisco is the best"}
