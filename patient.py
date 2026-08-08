from person import Person

class Patient(Person):
    def __init__(self, person_id, name, age, gender, phone, email, address,
                 patient_id, blood_group, medical_history, allergies,
                 emergency_contact, insurance_number, date_registered):
        super().__init__(person_id, name, age, gender, phone, email, address)
        self.patient_id = patient_id
        self.blood_group = blood_group
        self.medical_history = medical_history
        self.allergies = allergies
        self.emergency_contact = emergency_contact
        self.insurance_number = insurance_number
        self.date_registered = date_registered


    def get_details(self):
        base = super().get_details()
        return (
            f"{base}\n"
            f"Patient ID : {self.patient_id}\n"
            f"Madical History : {','.join(self.medical_history) if self.medical_history else 'None'}\n"
            f"Allergies : {','.join(self.allergies) if self.self.allergies else 'None'}\n"
            f"Emergency Contact : {self.emergency_contact}\n"
            f"Insurance No : {self.insurance_number}\n"
            f"Date Registered : {self.date_registered}"
        )
    def add_medical_histroy(self, condition):
        if condition not in self.medical_history:
            self.medical_history.append(condition)
            print(f"'{condition}' added to medical history.")
        else:
            print(f"'{condition}' already exists in medical history.")

    def __str__(self):
        return f"Patient: {self.name} (ID : {self.patient_id})"