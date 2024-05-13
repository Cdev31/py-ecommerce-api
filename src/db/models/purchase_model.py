from sqlalchemy import VARCHAR
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base

class PurchaseModel( Base ):
    __tablename__ = "products"