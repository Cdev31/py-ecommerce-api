from sqlalchemy import Column, text, UUID, VARCHAR, ForeignKey, INTEGER, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base

class PurchaseProductModel( Base ):
    __tablename__ = "purchase_product"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    purchaseId: Column = Column("purchase_id", UUID, ForeignKey("purchases.id"), nullable=False )

    productId: Column = Column("product_id", UUID, ForeignKey("products.id"), nullable=False )

    status: Column[str] = Column("status", VARCHAR, nullable=False )

    quantity: Column[int] = Column("quantity", INTEGER, nullable=False )
    
    price: Column[float] = Column("total", DECIMAL(precision=6, scale=2), nullable=False )

