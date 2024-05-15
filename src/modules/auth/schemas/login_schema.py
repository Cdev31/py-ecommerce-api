from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class LoginUserSchema( BaseModel ):
    
    email: EmailStr = Field()

    password: str = Field(pattern=r"^[A-Za-z0-9@!]{8,15}$")



class RegisterUserSchema( BaseModel ):
    
    fullName: str = Field(min_length=10)
    
    email: EmailStr = Field()
    
    dateOfBirth: datetime = Field()
    
    password: str = Field(pattern=r"^[A-Za-z0-9@!]{8,15}$")