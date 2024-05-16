from abc import ABC, abstractmethod
from typing import List, Any
from ...utils import ResponseType

class AuthInterface( ABC ):

    @abstractmethod
    def login(self, email:str, password: str ) -> ResponseType :
        pass

    @abstractmethod
    def register_user( self, data: Any ) -> ResponseType:
        pass
