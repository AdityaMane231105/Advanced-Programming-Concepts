records = [
    ["101", "Amit", 85],
    ["102", "Priya", 92],
    ["103", "Rahul", 78]
]

with open("students.csv", "w") as f:
    f.write("RollNo,Name,Marks\n")
    for roll, name, marks in records:
        f.write(f"{roll},{name},{marks}\n")

print("All records:")
for record in records:
    print(record)

highest = max(records, key=lambda x: x[2])
average = sum(x[2] for x in records) / len(records)

print("Highest marks:", highest)
print("Average marks:", average)
print("Students scoring more than 80:")

for record in records:
    if record[2] > 80:
        print(record)
