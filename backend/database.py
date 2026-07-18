from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URL, DATABASE_NAME

# Create MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

# Select the database
db = client[DATABASE_NAME]

# Create/access the users collection
users_collection = db["users"]

# Function to check MongoDB connection
async def connect_to_mongo():
    try:
        await client.admin.command("ping")
        print("✅ Connected to MongoDB")
        print(f"📂 Database: {DATABASE_NAME}")
    except Exception as e:
        print("❌ MongoDB Connection Failed")
        print(e)