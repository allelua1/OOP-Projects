class Course:
    def __init__(self, title, description, max_capacity = 30):
        self.title = title
        self.description = description
        self.max_capacity = max_capacity
        self.instructor = None
        self.students = []
        self.completed_students = []

    def add_student(self, student):
        if len(self.students) >= self.max_capacity:
            return False
        if student in self.students:
            return False
        self.students.append(student)
        return True

    def remove_student(self, student): 
        if student not in self.students:
            return False
        self.students.remove(student)
        return True

    def mark_completed(self, student):
        if student not in self.students:
            return False
        self.students.remove(student)
        self.completed_students.append(student)
        return True

    def assigninstructor(self, instructor):
        self.instructor = instructor
        return True

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.completed_courses = []

    def enroll(self, course):
        if course in self.enrolled_courses:
            return False
        if course.add_student(self):
            self.enrolled_courses.append(course)
            return True
        return False
    
    def unenroll(self, course):
        if course not in self.enrolled_courses:
            return False
        if course.remove_student(self):
            self.enrolled_courses.remove(course)
            return True
        return False
    def complete_course(self, course):
        if course not in self.enrolled_courses:
            return False
        if course.mark_completed(self):
            self.enrolled_courses.remove(course)
            self.completed_courses.append(course)
            return True
        return False

class Instructor:
    def __init__(self, name, email, expertise):
        self.name = name
        self.email = email
        self.expertise = expertise
        self.courses = []

    def assign_course(self, course):
        if course.assigninstructor(self):
            self.courses.append(course)
            return True   

# creating courses with different capacities

course1 = Course("Python Programming", "Introduction to Python programming.", 20)
course2 = Course("Data Science", "Advanced data analysis and machine learning techniques.")

print(f"Course 1: {course1.title}, Max Capacity: {course1.max_capacity}")
print(f"Course 2: {course2.title}, Max Capacity: {course2.max_capacity}")

# Test Student Enrollment
course = Course("Python Programming", "Introduction to Python programming.", 2)
student1 = Student("Allelua", "allelua@gmail.com")
student2 = Student("Benigne", "benigne@gmail.com")
student3 = Student("Diane", "diane@gmail.com")

# enroll students
print(student1.enroll(course))  # True
print(student2.enroll(course))  # True  
print(student3.enroll(course))  # False, course is full

# enrolling student again
print(student1.enroll(course))  # False, already enrolled

# check course and student
print(f"Course has {len(course.students)} students enrolled.")
print(f"Student has {len(student1.enrolled_courses)} courses enrolled.")

# student unenrollment
course = Course("Python Programming", "Introduction to Python programming.")
student = Student("Allelua", "allelua@gmail.com")

student.enroll(course)
print(student.unenroll(course))  # True
print(f"Student has {len(student.enrolled_courses)} courses enrolled.")

result = student.unenroll(course)  # False, not enrolled
print(result)  # False

# course completion
course = Course("Python Programming", "Introduction to Python programming.")
student = Student("Allelua", "allelua@gmail")

student.enroll(course)
print(f"Before completion: Enrolled Courses: {len(student.enrolled_courses)}, Completed Courses: {len(student.completed_courses)}")

student.complete_course(course)
print(f"After completion: Enrolled Courses: {len(student.enrolled_courses)}, Completed Courses: {len(student.completed_courses)}")