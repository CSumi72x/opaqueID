from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router
from database import connect_to_mongo

app = FastAPI(
    title="OPAQUE ID API",
    description="OPAQUE Authentication System Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://opaque-id-xoyp-eight.vercel.app",
        "https://opaque-id-xoyp-git-main-csumi72xs-projects.vercel.app",
        "https://opaque-id-xoyp-pz3xvky2l-csumi72xs-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB when the app starts
@app.on_event("startup")
async def startup():
    await connect_to_mongo()

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "OPAQUE ID Backend is running"
    }