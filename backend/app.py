from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router


app = FastAPI(
    title="OPAQUE ID API",
    description="OPAQUE Authentication System Backend",
    version="1.0.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://opaque-id-xoyp-eight.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "OPAQUE ID Backend is running"
    }