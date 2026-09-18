from student import details as s
from faculty import details as f
import marks

student_info = s.info()
faculty_info = f.info()
marks_info = marks.marks()

print("Student:", student_info["name"], student_info["id"], student_info["course"])
print("Faculty:", faculty_info["name"], faculty_info["id"], faculty_info["department"])
print("Marks:", marks_info["subject"], marks_info["score"])
