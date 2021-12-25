from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.server.database import (
    add_secret,
    delete_secret,
    retrieve_secret,
    retrieve_secrets,
    update_secret,
)
from app.server.model.secret import (
    error_response_model,
    response_model,
    SecretSchema,
    UpdateSecretModel,
)

router = APIRouter()


@router.post("/", response_description="Secret data added into the database")
async def add_secret_data(secret: SecretSchema = Body(...)):
    secret = jsonable_encoder(secret)
    new_secret = await add_secret(secret)
    return response_model(new_secret, "Secret added successfully.")

