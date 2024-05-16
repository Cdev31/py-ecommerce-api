from typing import Any
from ..interface import AuthInterface


class AuthService:
   
    def __init__(self, 
    authAdapter: AuthInterface            
    ):
     self.authAdapter = authAdapter

    def loginUser( self, email: str, password: str ):
        return self.authAdapter.login( email, password )
    
    def registerUser( self, data: Any ):
       return self.authAdapter.register_user( data )