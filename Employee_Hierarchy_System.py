class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    def introduce(self):
        return super().introduce() + f"I work with employee ID {self.employee_id}."
    def calculate_paycheck(self):
        return self.salary / 12
    
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
    def calculate_paycheck(self):
        return super().calculate_paycheck() + (self.salary *1.2) /12
    def manage_team(self):
        return f"Managing the {self.department} department."

class Engineer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language
    def code(self):
        return f"Coding in {self.programming_language}."



# Test your implementation

person = Person("Benigne Ngerituje", 24)
employee = Employee("Allelua Ally", 23, "E670449", 6000000 )
manager = Manager("Bob Williams", 45, "M1234", 76000000, "Marketing")
engineer = Engineer("Carol David", 28, "E674764", 7400009, "Python")

print(person.introduce())
print(employee.introduce())
print(f"Monthly pay: ${employee.calculate_paycheck()}")
print(manager.manage_team())
print(manager.calculate_paycheck())
print(engineer.code())