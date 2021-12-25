from typing import Optional
from pydantic import BaseModel, Field


class SecretSchema(BaseModel):
    id_secret: int = Field(...)
    text: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id_secret": "1...n",
                "text": "you will never guess",
                "password": "qwerty",
            }
        }


class UpdateSecretModel(BaseModel):
    id_secret: Optional[int]
    text: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id_secret": "1...n",
                "text": "you will never guess",
                "password": "qwerty",
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
