from fastapi import APIRouter, Body
from typing import Annotated
from .schemas.login_schema import LoginUserSchema, RegisterUserSchema
from .services import AuthService, AuthAdapter 

authServices = AuthService( AuthAdapter() )
auth_router: APIRouter = APIRouter()



@auth_router.post("/login")
def loginUser( data: Annotated[ LoginUserSchema, Body() ] ):
    data = authServices.loginUser( data.email, data.password )
    return data

@auth_router.post("/register")
def registerUser( data: Annotated[ RegisterUserSchema, Body() ] ):
    data = authServices.registerUser( data )
    return data