from salary import gross_salary, deductions, net_salary
 
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
 
print("Gross salary:", gross_salary(basic, allowance))
print("Deductions:", deductions(basic))
print("Net salary:", net_salary(basic, allowance))
