def total(marks):
    return sum(marks)
 
def percentage(marks):
    return total(marks) / len(marks)
 
def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    return "F"
