from abc import ABC, abstractmethod
from typing import List, Any


class AuthInterface( ABC ):

    @abstractmethod
    def login(self, email:str, password: str ):
        pass

    @abstractmethod
    def register_user( self, data: Any ):
        pass
