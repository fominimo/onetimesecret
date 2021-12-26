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


@router.get("/", response_description="Secrets retrieved")
async def get_secrets():
    secrets = await retrieve_secrets()
    if secrets:
        return response_model(secrets, "Secrets data retrieved successfully")
    return response_model(secrets, "Empty list returned")


@router.get("/{id}", response_description="Secret data retrieved")
async def get_secret_data(id):
    secret = await retrieve_secret(id)
    if secret:
        return response_model(secret, "Student data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Student doesn't exist.")


@router.put("/{id}")
async def update_secret_data(id: str, req: UpdateSecretModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_secret = await update_secret(id, req)
    if updated_secret:
        return response_model(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Secret data deleted from the database")
async def delete_secret_data(id: str):
    deleted_secret = await delete_secret(id)
    if deleted_secret:
        return response_model(
            "Secret with ID: {} removed".format(id), "Secret deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Secret with id {0} doesn't exist".format(id)
    )
