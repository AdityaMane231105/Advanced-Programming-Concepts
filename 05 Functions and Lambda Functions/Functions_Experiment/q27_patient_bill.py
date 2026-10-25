def consultation_charges(visits, rate):
    return visits * rate


def laboratory_charges(tests):
    return sum(tests)


def medicine_charges(medicines):
    return sum(medicines)


def room_charges(days, daily_rate):
    return days * daily_rate


def final_bill(category, consultation, laboratory, medicine, room):
    subtotal = consultation + laboratory + medicine + room
    discount_rates = {"general": 0.0, "senior": 0.10, "staff": 0.15}
    discount = subtotal * discount_rates.get(category.lower(), 0.0)
    return {"subtotal": subtotal, "discount": discount, "total": subtotal - discount}


consultation = consultation_charges(2, 500)
laboratory = laboratory_charges([800, 450])
medicine = medicine_charges([300, 250])
room = room_charges(3, 1200)
print(final_bill("senior", consultation, laboratory, medicine, room))
