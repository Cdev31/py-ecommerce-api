import bcrypt



def hashed_password( password: str ) -> str:
    
    encoded: bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw( encoded, salt )

    return hashed_password.decode('utf-8')


def verify_password( password: str, hashed: str ) -> bool:

    password_bytes: bytes = password.encode('utf-8')

    hashed_password = hashed.encode('utf-8')

    return bcrypt.checkpw( password_bytes, hashed_password )
