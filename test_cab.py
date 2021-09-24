from cab_invoice import CabInvoice


def test_fare():
    cab = CabInvoice()
    assert cab.calculate_fare(2, 5) == 25
    assert cab.calculate_fare(0.1, 1) == 5
