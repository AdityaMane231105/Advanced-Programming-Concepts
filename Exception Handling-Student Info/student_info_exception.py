class InvalidInputError(Exception):
    pass

def get_student_info():
    try:
        name = input("Enter student name: ")
        if name.isdigit():
            raise InvalidInputError("Name must be characters only.")

        roll = input("Enter roll number: ")
        if not roll.isdigit():
            raise InvalidInputError("Roll number must be numeric.")

        subjects = ["APC", "DAA", "AJT", "PEC-I"]
        marks = {}
        for sub in subjects:
            val = input(f"Enter marks for {sub}: ")
            if not val.isdigit():
                raise InvalidInputError(f"Marks for {sub} must be numeric.")
            marks[sub] = int(val)

        total = sum(marks.values())
        percentage = total / len(subjects)
        print("\nStudent Information")
        print("Name:", name)
        print("Roll Number:", roll)
        print("Marks:", marks)
        print("Total:", total)
        print("Percentage:", percentage)

    except InvalidInputError as e:
        print("Exception occurred:", e)
    finally:
        print("Execution complete.")

get_student_info()

