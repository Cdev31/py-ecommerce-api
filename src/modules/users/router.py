from fastapi import APIRouter, Body, Path
from .services import UserService, UserAdapter

userService = UserService( UserAdapter() )

user_router = APIRouter()


@user_router.get("/")
def findAllUsers():
    return { } 


@user_router.get("/{id}")
def findUserById( id = Path() ):
    return { } 


@user_router.post("/")
def createUser( data = Body()):
    return { } 