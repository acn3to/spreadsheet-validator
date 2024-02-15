import pytest
from datetime import datetime
from src.contract import Sales
from pydantic import ValidationError


def test_sales_with_valid_data():
    valid_data = {
        "email": "buyer@example.com",
        "date": datetime.now(),
        "value": 100.50,
        "product": "Product X",
        "quantity": 3,
        "category": "category1",
    }

    sale = Sales(**valid_data)

    assert sale.email == valid_data["email"]
    assert sale.date == valid_data["date"]
    assert sale.value == valid_data["value"]
    assert sale.product == valid_data["product"]
    assert sale.quantity == valid_data["quantity"]
    assert sale.category == valid_data["category"]


def test_sales_with_invalid_data():
    invalid_data = {
        "email": "buyer",
        "date": "not a date",
        "value": -100,
        "product": "",
        "quantity": -1,
        "category": "category3"
    }

    with pytest.raises(ValidationError):
        Sales(**invalid_data)


def test_category_validation():
    data = {
        "email": "buyer@example.com",
        "date": datetime.now(),
        "value": 100.50,
        "product": "Product Y",
        "quantity": 1,
        "category": "non-existent category",
    }

    with pytest.raises(ValidationError):
        Sales(**data)
