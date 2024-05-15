from datetime import datetime, timedelta
from jose import JWTError, jwt  # type: ignore
from fastapi import HTTPException
from typing import Optional
from ..config.config import config



def create_access_token( payload: dict, expires_delta: Optional[timedelta] = None ):
    
    to_encode = payload.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta( minutes=60 ) 

    to_encode.update({ "exp": expire })

    encoded_jwt = jwt.encode( to_encode, config["secret_key"], algorithm=config["algorithm"] )
  
    return encoded_jwt       


def verify_access_token( token: str ):
    
    credential_exception = HTTPException(
        status_code=401,
        detail="Colud not validate credentials",
        headers={"WWW-Authenticated": "Bearer"}
    )
    try:
    
        payload = jwt.decode( token, config["secret_key"], algorithms=config["algorithm"] )
    
        email: str = payload.get("sub")
    
        if email is None:
        
            raise credential_exception
    
    except JWTError:

        
        raise credential_exception
    return payload['email']