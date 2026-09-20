from fastapi import FastAPI
from app.config import Settings
app = FastAPI(
    title=Settings.app_name
)


@app.get("/")
def root():
    return {"message": f"{Settings.app_name}"}


@app.get("/health")
def health_check():
    return {"status":"health",
            "envirnment":Settings.environment
    }