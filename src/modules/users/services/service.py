from typing import Any
from ..interface import UserInterface


class UserService():

    userAdapter: UserInterface
    
    def __init__(self, 
       userAdapter: UserInterface            
    ):
        userAdapter = userAdapter

    def findUsers( self ):
        return self.userAdapter.find()
    
    def findUserById( self, id: str ):
        return self.userAdapter.find_by_id( id )
    
    def createUser( self, data: Any ):
        return self.userAdapter.create( data )
    
    def updateUser( self, id: str, data: Any ):
        return self.userAdapter.update( id, data )
    
    def deleteUser( self, id: str ):
        return self.userAdapter.delete( id )
