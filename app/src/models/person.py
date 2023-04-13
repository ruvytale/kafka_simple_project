from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    id: str
    name: str
    title: str
    email: EmailStr
