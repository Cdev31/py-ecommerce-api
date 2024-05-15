from sqlalchemy import VARCHAR, Column, text, CheckConstraint, UUID, ForeignKey
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

    userId: Column = Column("userId",UUID, ForeignKey('users.id'), unique=True )

    addres: Column[str] = Column("address", VARCHAR, nullable=False )

    phoneNumber: Column = Column("phone_number", VARCHAR, nullable=False)

    __table_args__: tuple[CheckConstraint] = (
        CheckConstraint(
            r"phone_number ~ '\^\+503\s[0-9]{4}-[0-9]{4}$'",
            name="check_phone_number"
        ),
    )