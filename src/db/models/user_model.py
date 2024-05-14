from sqlalchemy import VARCHAR, Column, text, TIMESTAMP, BOOLEAN, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base
from datetime import datetime

class UserModel( Base ):
    __tablename__ = "users"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    fullName: Column[str] = Column("full_name", VARCHAR, nullable=False)

    dateOfBirth: Column[datetime] = Column("date_of_birth", TIMESTAMP, nullable=False )

    email: Column[str] = Column("email", VARCHAR, nullable=False, unique=True)

    password: Column[str] = Column("password", VARCHAR, nullable=True, unique=True)

    google: Column[bool] = Column("google", BOOLEAN, nullable=True)

    __table_args__= (
        CheckConstraint(
            r"email ~ '\^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$\'",
            name="email_constraint"
        )
    )