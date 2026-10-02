from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import AsyncSessionLocal
from app.models import ProjectCreate, ProjectResponse
from app.models import Project as ProjectModel

router = APIRouter(prefix="/projects", tags=["projects"])


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@router.get("/", response_model=list[ProjectResponse])
async def list_projects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProjectModel))
    return result.scalars().all()


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(payload: ProjectCreate, db: AsyncSession = Depends(get_db)):
    project = ProjectModel(
        title=payload.title,
        description=payload.description,
        github_url=payload.github_url,
        category=payload.category,
        owner_id="00000000-0000-0000-0000-000000000001",
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project
