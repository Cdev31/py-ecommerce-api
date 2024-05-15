from ..interface import AuthInterface
from sqlalchemy.future import select
from ....db.libs.conecction import SessionLocal
from ....db.models.user_model import UserModel
from ...helpers.encrypt_password import hashed_password, verify_password
from ....utils.generate_jwt import create_access_token



class AuthAdapter( AuthInterface ):
     
    db = SessionLocal()


    def login(self, email:str, password: str ):
        
        exitsUser = self.db.execute( 
            select( UserModel ).where( UserModel.email == email) ).scalar_one_or_none()
        
        if exitsUser is None:
            return 

        if verify_password( str(exitsUser.password), password ) == False :
            return
        
        newToken = create_access_token({
            'id': exitsUser.id,
            'email': exitsUser.email
        })

        return newToken

        
    def register_user( self, data: dict ):
        
        newUser = data.copy()
        
        newPassword = hashed_password( data['password'])

        newUser.update({"password": newPassword })
        
        self.db.add( UserModel( newUser ) )

        self.db.commit()
        