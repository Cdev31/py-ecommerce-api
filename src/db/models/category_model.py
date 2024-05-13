from sqlalchemy import Column, VARCHAR , text
from sqlalchemy.dialects.postgresql import UUID as PsqlUUID
from ..libs.conecction import Base



class CategoryModel( Base ):
    ___tablename__ = "categories"

    id = Column(
        PsqlUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=text("gen_random_uuid()")
    )

    categoryName: Column[str] = Column("category_name", VARCHAR, nullable=False )

    description: Column[str]  = Column("description", VARCHAR, nullable=False)

    