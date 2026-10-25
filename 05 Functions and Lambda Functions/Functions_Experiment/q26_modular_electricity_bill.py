def energy_charge(units):
    first = min(units, 100) * 1.5
    second = max(min(units - 100, 100), 0) * 2.5
    third = max(units - 200, 0) * 4.0
    return first + second + third


def electricity_bill(units):
    if units < 0:
        raise ValueError("units must be non-negative")
    fixed_charge = 50.0
    discount = 0.10 * energy_charge(units) if units < 100 else 0.0
    taxable_amount = fixed_charge + energy_charge(units) - discount
    tax = taxable_amount * 0.05
    return {
        "energy_charge": energy_charge(units),
        "fixed_charge": fixed_charge,
        "discount": discount,
        "tax": tax,
        "total": taxable_amount + tax
    }


print(electricity_bill(250))
