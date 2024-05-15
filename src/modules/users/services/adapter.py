from ..interface import UserInterface
from typing import Any

class UserAdapter(UserInterface):
     
    def find(self):
        pass
   
    def find_by_id(self, id: str ):
        pass
    
    def create( self, data: Any ):
        pass

    def update(self, id: str, data: Any):
        pass

    def delete( self, id: str ):
        pass