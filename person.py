class Person:
    def __init__(self, person_id, name, age, gender, phone, email, address ):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
    def get_details(self):
        return (
            f"ID : {self.person_id}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age}\n"
            f"Gender : {self.gender}\n"
            f"Phone : {self.phone}\n "
            f"Email : {self.email}\n"
            f"Address : {self.address}"
        )
    def __str__(self):
        return f"{self.person_id} - {self.name}"