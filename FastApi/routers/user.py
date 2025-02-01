from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from FastApi.backend.db import SessionLocal
from FastApi.backend.db_depends import get_db
from typing import Annotated
from FastApi.models.user import User
from FastApi.schemas import UserCreate, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_router = APIRouter(prefix="/user", tags=["user", ])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Эндпоинт регистрации
@user_router.post("/register/")
def register(user: UserCreate):
    db = SessionLocal()
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully!"}

# Эндпоинт авторизации
@user_router.post("/login/")
def login(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": f"Welcome back, {user.username}!"}

