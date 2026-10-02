from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: str = "student"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)


class ProfileCreate(BaseModel):
    full_name: str | None = None
    bio: str | None = None
    skills: str | None = None
    degree_program: str | None = None
    github_url: str | None = None
    linkedin_url: str | None = None


class ProfileResponse(ProfileCreate):
    id: UUID
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)


class ProjectCreate(BaseModel):
    title: str
    description: str | None = None
    github_url: str | None = None
    category: str | None = None


class ProjectResponse(ProjectCreate):
    id: UUID
    owner_id: UUID

    model_config = ConfigDict(from_attributes=True)


class EventCreate(BaseModel):
    title: str
    description: str | None = None
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None


class EventResponse(EventCreate):
    id: UUID
    created_by: UUID | None = None

    model_config = ConfigDict(from_attributes=True)


class ResourceCreate(BaseModel):
    title: str
    description: str | None = None
    resource_type: str | None = None
    url: str | None = None


class ResourceResponse(ResourceCreate):
    id: UUID
    uploaded_by: UUID | None = None

    model_config = ConfigDict(from_attributes=True)
