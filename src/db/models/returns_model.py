from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base

class ReturnModel( Base ):
    __tablename__ = "products"