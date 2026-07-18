from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router   # change this import if your router file name is different

app = FastAPI()

# CORS configuration for Vercel + Local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://opaque-id-xoyp-eight.vercel.app",
        "https://opaque-id-xoyp.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include your API routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "OPAQUE ID Backend is running"
    }