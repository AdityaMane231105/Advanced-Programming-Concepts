import pandas as pd

data = pd.read_csv("student_marks.csv")
marks_series = pd.Series(data["Marks"], index=data["Name"], name="Student Marks")
print(marks_series)
