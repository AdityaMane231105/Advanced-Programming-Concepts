def gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    return basic_salary + hra + da


print(gross_salary(30000))
