from fastapi import FastAPI
from app.config import settings
from app.api.users import router as users_router
from app.api.research import router as research_router

app = FastAPI(
    title=settings.app_name,
    description="Backend Api for AI-Powered enterprie research agent",
    version="1.0.0"
)
app.include_router(users_router)
app.include_router(research_router)




@app.get("/")
def root():
    return {"message": f"{settings.app_name} App is running"}


@app.get("/health")
def health_check():
    return {"status":"health",
            "envirnment":settings.environment,
    }