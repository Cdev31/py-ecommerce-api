from abc import ABC, abstractmethod
from typing import List, Any


class UserInterface( ABC ):

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def find_by_id(self, id: str ):
        pass

    @abstractmethod
    def create( self, data: Any ):
        pass

    @abstractmethod
    def update(self, id: str, data: Any):
        pass

    @abstractmethod
    def delete( self, id: str ):
        pass