from sqlalchemy import VARCHAR, Column, text, INTEGER, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base

class ProductModel( Base ):
    __tablename__ = "products"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    productName: Column[str] = Column("product_name", VARCHAR, nullable=False )

    description: Column[str] = Column("description", VARCHAR, nullable=False )

    stock: Column[int] = Column("stock", INTEGER, nullable=False, default=0)

    internalReference: Column[str] = Column("internal_reference", VARCHAR, nullable=False )

    price: Column[float] = Column("price", DECIMAL(precision=6, scale=2), nullable=False, default=0.00)

    cost: Column[float] = Column("cost", DECIMAL(precision=6, scale=2), nullable=False, default=0.00)

    taxt: Column[int] = Column("taxt", INTEGER, nullable=False )

    discount: Column[int] = Column("discount", INTEGER, nullable=False )
