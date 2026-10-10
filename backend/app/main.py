from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SmartCampus AI - API",
    description="Plateforme agentique d'orientation universitaire",
    version="1.0.0"
)

# CORS setup bech React y'connecti mn ghir blocage
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartCampus AI Backend API"}

