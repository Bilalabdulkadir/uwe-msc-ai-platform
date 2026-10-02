from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["api"])


@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "uwe-msc-ai-platform"}
