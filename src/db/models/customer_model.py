from sqlalchemy import VARCHAR, Column, text, TIMESTAMP, BOOLEAN, UUID,ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base
from datetime import datetime

class CustomerModel( Base ):
    __tablename__ = "customers"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    userId: Column = Column("userId",UUID, ForeignKey('users.id'), unique=True)
    addres: Column[str] = Column()
    phoneNumber: Column = Column()
    
   
