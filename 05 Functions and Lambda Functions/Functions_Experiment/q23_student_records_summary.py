def grade_for(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"


def process_students(records):
    results = []
    for record in records:
        total = sum(record["marks"])
        percentage = total / 5
        results.append({
            "name": record["name"],
            "roll_number": record["roll_number"],
            "total": total,
            "percentage": percentage,
            "grade": grade_for(percentage)
        })
    if not results:
        raise ValueError("records must not be empty")
    class_average = sum(student["percentage"] for student in results) / len(results)
    highest = max(results, key=lambda student: student["percentage"])
    lowest = min(results, key=lambda student: student["percentage"])
    return results, class_average, highest, lowest


students = [
    {"name": "Asha", "roll_number": 1, "marks": [88, 91, 84, 90, 87]},
    {"name": "Rahul", "roll_number": 2, "marks": [72, 75, 70, 78, 74]},
    {"name": "Meera", "roll_number": 3, "marks": [95, 93, 97, 91, 96]}
]
print(process_students(students))
