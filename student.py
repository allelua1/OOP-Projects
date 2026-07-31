class Student:
    def __init__(self, student_id, name, enrolled = True):
        # TODO: Initialize private attributes with double underscore prefix
        # TODO: Create __id as a private attribute and assign student_id to it
        # TODO: Create __grades as an empty dictionary to store course grades
        # TODO: Create __enrolled and assign the enrolled parameter to it
        # TODO: Use the name sette__r for validation by assigning name parameter to self.name
        self.__id = student_id
        self.__grades = {}
        self.__enrolled = enrolled
        self.name = name

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self.__name = value
            return
        raise ValueError("Name must be at least 2 characters long.")
    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
         if isinstance(value, bool):
            self.__enrolled = value
         raise ValueError("Enrolled must be a boolean value.")

    @property
    def grade_average(self):
        # TODO: Check if __grades is empty, return 0 if it is
        # TODO: Calculate and return the average of all grades in the __grades dictionary
        # TODO: Use sum(self.__grades.values()) / len(self.__grades) for the calculation
        if not self.__grades:
            return 0
        average = sum(self.__grades.values()) / len(self.__grades)
        return average

    def add_grade(self, course, grade):
            # TODO: Add a grade for a course by adding a key-value pair to the __grades dictionary
        # TODO: Use course as the key and grade as the value
        self.__grades[course]=grade

    def display_record(self):
        if self.__enrolled:
            enrolled_status = "Yes"
        enrolled_status = "No"
        
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Enrolled: {enrolled_status}")
        print(f"Courses: {len(self.__grades)}")
        print(f"Grade Average: {self.grade_average:.2f}")

class StudentRegistry:
    def __init__(self):
        self.__students = {}

    def add_student(self, student):
         # TODO: Add a student to the registry by using student.id as the key
        # TODO: Store the student object as the value in the __students dictionary
        self.__students[student.id] = student

    def remove_student(self, student_id):
        if student_id in self.__students.keys():
            del self.__students[student_id]

    def get_student(self, student_id):
        # TODO: Return the student with the given student_id from the __students dictionary
        # TODO: Use the .get() method to safely retrieve the student (returns None if not found)
        if student_id in self.__students.keys():
            return self.__students.get(student_id)
        return None
    def get_top_student(self):
        # TODO: Check if the __students dictionary is empty, return None if it is
        # TODO: Use max() with a key function to find the student with the highest grade_average
        # TODO: The key function should be a lambda that returns student.grade_average
        if not self.__students:
            return None
        return max(self.__students.values(), key = lambda student: student.grade_average)

    def display_all(self):
         # TODO: Loop through all student_id, student pairs in the __students dictionary
        # TODO: For each student, print a formatted string with ID, name, and grade average
        # TODO: Format: "ID: {student_id}, Name: {student.name}, Average: {student.grade_average:.2f}"
        for student_id, student in self.__students.items():
            print(f"ID: {student_id}\tName: {student.name}\t Average: {student.grade_average} ")
    

    
student1 = Student(1001, "Alice Smith")
student2 = Student(1002, "Bob Benigne")
student3 = Student(1003, "Allelua Ally")

#add grades
student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student1.add_grade("Economics", 92)

student2.add_grade("Math", 80)
student2.add_grade("Science", 75)
student2.add_grade("Economics", 82)

student3.add_grade("Math", 70)
student3.add_grade("Science", 95)
student3.add_grade("Economics", 90)

# display student records
print("\n------------Student Record-----------\n")
student1.display_record()
print()
student2.display_record()
print()
student3.display_record()
print()

# test name validation

try:
    student1.name = "J"
except ValueError as e:
    print(f"Name validation error: {e}")
print()

# create registry and add students
registry = StudentRegistry()
registry.add_student(student1)
registry.add_student(student2)
registry.add_student(student3)

# display all student
print("All student in registry: ")
registry.display_all()

# get top student
top_student = registry.get_top_student()
print(f"Top Student: {top_student.name} (Average: {top_student.grade_average})")

# remove a student
registry.remove_student(1002)
print("\
      After removing student 1002: ")
registry.display_all()
