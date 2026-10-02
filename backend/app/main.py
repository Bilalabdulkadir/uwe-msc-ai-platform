from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.projects import router as project_router

app = FastAPI(title="UWE MSc AI Platform", version="1.0.0")

app.include_router(health_router)
app.include_router(project_router)


@app.get("/")
async def root():
    return {"message": "UWE MSc AI Platform API is running"}
