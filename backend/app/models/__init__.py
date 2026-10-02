from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), default="student")
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    github_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=None)

    profile: Mapped["Profile | None"] = relationship(back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    skills: Mapped[str | None] = mapped_column(Text, nullable=True)
    degree_program: Mapped[str | None] = mapped_column(String(255), nullable=True)
    github_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    user: Mapped[User] = relationship(back_populates="profile")


class Discussion(Base):
    __tablename__ = "discussions"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=None)


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    start_date: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    end_date: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_by: Mapped[str | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=None)


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    github_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    owner_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"))
    category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=None)


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    resource_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    uploaded_by: Mapped[str | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=None)
