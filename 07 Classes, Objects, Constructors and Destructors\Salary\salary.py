def gross_salary(basic, allowance):
    return basic + allowance
 
def deductions(basic):
    return basic * 0.1
 
def net_salary(basic, allowance):
    gross = gross_salary(basic, allowance)
    return gross - deductions(basic)
