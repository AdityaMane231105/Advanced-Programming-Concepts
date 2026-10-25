try:
    from .student.details import student_info
    from .student.marks import student_marks
    from .faculty.details import faculty_info
except ImportError:
    from student.details import student_info
    from student.marks import student_marks
    from faculty.details import faculty_info

print(student_info())
print(student_marks())
print(faculty_info())
