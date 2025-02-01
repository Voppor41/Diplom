from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int