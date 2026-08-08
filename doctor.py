from person import Person
class Doctor(Person):
    def __init__(self, person_id, name, age, gender, phone, email, address,
                 doctor_id, specialization, department, qualification, 
                 experience_year, available_days, consultation_fee):
        super().__init__(person_id, name, age, gender, phone, email, address)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.department = department
        self.qualification = qualification
        self.experience_year = experience_year
        self.available_days = available_days
        self.consultation_fees = consultation_fee

    def get_details(self):
        base =  super().get_details()
        return (
            f"{base}\n"
            f"Doctor ID : {self.doctor_id}\n"
            f"Specialization : {self.specialization}\n"
            f"Department : {self.department}\n"
            f"Qualification : {self.qualification}"
            f"Experience : {self.experience_year} years \n"
            f"Available days : {','.join(self.available_days)}\n"
            f"COnsultation Fees: KES {self.consultation_fees}"
        )

    def is_available(self, day):
        return day in self.available_days

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"
