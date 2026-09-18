def total(marks): return sum(marks)
def percentage(marks): return sum(marks)/len(marks)
def grade(marks): return 'A' if percentage(marks) >= 75 else 'B' if percentage(marks) >= 50 else 'C'    


