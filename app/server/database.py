import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.secrets
secret_collection = database.get_collection("secrets_collection")


# helpers
def secret_helper(secret) -> dict:
    return {
        "id": str(secret["_id"]),
        "id_secret": str(secret["id"]),
        "text": secret["text_secret"],
        "password": secret["pass"],
     }


# Retrieve all secrets present in the database
async def retrieve_secrets():
    secrets = []
    async for secret in secret_collection.find():
        secrets.append(secret_helper(secret))
    return secrets


# Add a new secret into to the database
async def add_secret(secret_data: dict) -> dict:
    secret = await secret_collection.insert_one(secret_data)
    new_secret = await secret_collection.find_one({"_id": secret.inserted_id})
    return secret_helper(new_secret)


# Retrieve a secret with a matching ID
async def retrieve_secret(id: str) -> dict:
    secret = await secret_collection.find_one({"_id": ObjectId(id)})
    if secret:
        return secret_helper(secret)


# Update a secret with a matching ID
async def update_secret(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    secret = await secret_collection.find_one({"_id": ObjectId(id)})
    if secret:
        updated_secret = await secret_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_secret:
            return True
        return False


# Delete a student from the database
async def delete_secret(id: str):
    secret = await secret_collection.find_one({"_id": ObjectId(id)})
    if secret:
        await secret_collection.delete_one({"_id": ObjectId(id)})
        return True
