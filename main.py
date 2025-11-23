from fastapi import FastAPI
from pydantic import BaseModel
from parser import parse_address


class AddressInput(BaseModel):
    address: str


app = FastAPI()


@app.post("/parse")
def libpostal(data: AddressInput):
    result = parse_address(data.address)

    parsed = {}
    for value, label in result:
        parsed[label] = value

    return {
        "original": data.address,
        "parsed": parsed
    }
