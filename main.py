from fastapi import FastAPI
from pydantic import BaseModel

class AddressInput(BaseModel):
    address: str

app = FastAPI()

@app.post("/parse")
def parse_address_endpoint(data: AddressInput):
    return {
        "original": data.address,
        "parsed": {
            "house_number": "fake",
            "road": "fake",
            "city": "fake",
            "postcode": "fake"
        }
    }

