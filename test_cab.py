import pytest

from cab_invoice import Ride, InvoiceGenerator

invoice_generator = InvoiceGenerator()


def test_calculate_fare():
    assert Ride(2, 5, 1).calculate_fare() == 25
    assert Ride(2, 5, 2).calculate_fare() == 20


def test_invalid_input():
    with pytest.raises(BaseException):
        assert Ride.calculate_fare('s', 's', 's')

def test_object():
    assert (isinstance(invoice_generator, InvoiceGenerator))

