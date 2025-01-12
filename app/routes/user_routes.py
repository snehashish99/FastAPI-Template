from fastapi import APIRouter
from db import User
import asyncpg
from utils import database
from sqlalchemy import select
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/users")
async def get_users():
    users =  await database.fetch_all(select(User))
    return {"message": "List of users", "data": users}


@router.post("/users")
async def create_user(email: str, first_name: str, last_name: str):
    try:
        inserted_id = await database.execute(
            query=User.__table__.insert().values({'email': email, 'first_name': first_name, 'last_name': last_name}).returning(User.id)
        )
        return JSONResponse(status_code=200, content = {"message": "User created", 'id': inserted_id})
    except asyncpg.exceptions.UniqueViolationError:
        return JSONResponse(status_code=400, content = {"message": "Email exists"})
    except Exception:
        return JSONResponse(status_code=400, content = {"message": "Some error"})
