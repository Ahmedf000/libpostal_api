from fastapi import FastAPI
from pydantic import BaseModel

class AddressInput(BaseModel):
    address: str

app = FastAPI()
@app.post("/parse") #endpoint
def libpostal(data: AddressInput): #user parameter
    return {
        "The address": data.address,
        "Parsed": {
            "house_number": data.house_number,
            "street_number": data.street_number,
            "postal_code": data.postal_code,
            "district": data.district,
            "city": data.city,
            "country": data.country,
        }
    } #what we return

