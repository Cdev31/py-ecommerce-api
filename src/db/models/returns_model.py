from sqlalchemy import VARCHAR, Column, text, UUID, ForeignKey, TIMESTAMP, TIME, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base
from datetime import datetime

class ReturnModel( Base ):
    __tablename__ = "returns"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    customer: Column = Column("customer", UUID, ForeignKey("customers.id"), nullable=False )

    returnDate: Column[datetime] = Column("return_date", TIMESTAMP, nullable=False )

    returnHour: Column[datetime.hour] = Column("return_hour", TIME, nullable=False )

    deliveryAddress: Column[str] = Column("delivery_address", VARCHAR, nullable=False )

    reason: Column[str] = Column("reason", VARCHAR, nullable=False )

    status: Column[str] = Column("status", VARCHAR, nullable=False )

    total: Column[float] = Column("total", DECIMAL(precision=6, scale=2), nullable=False )

