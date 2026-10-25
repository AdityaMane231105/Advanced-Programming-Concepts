attendance = {
    "Mon": {"Alice", "Bob"},
    "Tue": {"Alice", "Charlie"},
    "Wed": {"Alice", "Bob", "Charlie"},
    "Thu": {"Bob"},
    "Fri": {"Alice", "Bob"}
}

all_days = set(attendance["Mon"])
for day in attendance.values():
    all_days &= day

one_day = set()
for student in set.union(*attendance.values()):
    count = sum(student in day for day in attendance.values())
    if count == 1:
        one_day.add(student)

unique_students = set.union(*attendance.values())

print("Attended all classes:", all_days)
print("Attended only one class:", one_day)
print("Total unique students:", unique_students)

