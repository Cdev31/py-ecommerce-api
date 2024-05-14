from sqlalchemy import VARCHAR, Column, text, UUID, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base

class ProductImageModel( Base ):
    __tablename__ = "products"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    productId: Column = Column("product_id", UUID, ForeignKey("products.id"))

    imageUrl: Column[str] = Column("image_url", VARCHAR, nullable=False )
