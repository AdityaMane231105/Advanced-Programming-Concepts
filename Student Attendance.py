students = [
    ["101", "Amit", 72, 80],
    ["102", "Priya", 90, 100],
    ["103", "Rahul", 60, 90]
]

with open("attendance.txt", "w") as f:
    for s in students:
        f.write(f"{s[0]},{s[1]},{s[2]},{s[3]}\n")

for roll, name, present, total in students:
    percentage = present / total * 100
    print(name, percentage, "%")
    if percentage < 75:
        print(name, "has attendance below 75%")

