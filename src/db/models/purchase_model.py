from sqlalchemy import VARCHAR, Column, text, UUID, ForeignKey, TIMESTAMP, TIME, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base
from datetime import datetime

class PurchaseModel( Base ):
    __tablename__ = "purchases"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    customer: Column = Column("customer", UUID, ForeignKey("customers.id"), nullable=False )

    purchaseDate: Column[datetime] = Column("purchase_date", TIMESTAMP, nullable=False )

    purchaseHour: Column[datetime.hour] = Column("purchase_hour", TIME, nullable=False )

    deliverDate: Column[datetime] = Column("deliver_date", TIMESTAMP, nullable=False )

    deliveryAddress: Column[str] = Column("delivery_address", VARCHAR, nullable=False )

    total: Column[float] = Column("total", DECIMAL(precision=6, scale=2), nullable=False )

