from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"

class Sales(BaseModel):
    """
    Data model for sales.

    Args:
        email (str): buyer's email
        date (datetime): date of purchase
        value (int): purchase value
        product (str): product name
        quantity (int): quantity of products
        category (str): product category

    """
    email: EmailStr
    date: datetime
    value: PositiveFloat
    product: str
    quantity: PositiveInt
    category: CategoryEnum

    @field_validator('category')
    def category_must_be_in_enum(cls, v):
        if v not in CategoryEnum:
            raise ValueError("Invalid category")
        return v
