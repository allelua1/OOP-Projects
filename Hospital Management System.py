import datetime
class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def get_details(self):
        return f"Patient ID: {self.patient_id} \t Name: {self.name} \t Age: {self.age }\t Gender: {self.gender} \t Disease: {self.disease}"

class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
    def add_patient(self, patient_id, name, age, gender, disease):
        if patient_id in self.patients:
            print(f"Patient with ID {patient_id} already exists.")
            return
        new_patient = Patient(patient_id, name,age, gender, disease )
        self.patients[patient_id] = new_patient
        print (f"\nPatient '{name}' added successfully.")

    def display_patients(self):
        if not self.patients:
            print(f"No patients currently in the system.")
            return
        print("\n----Current Patients Record----")
        for patient in self.patients.values():
            print(patient.get_details())

    def search_patient(self, patient_id):
        patient = self.patients.get(patient_id)

        if patient:
            print(f"\n Patient Found: \n{patient.get_details()}")
        else:
            print(f"\n Patient with ID {patient_id} not found.")

    def discharge_patient(self, patient_id):
        if patient_id in self.patients:
            discharged_patient = self.patients.pop(patient_id)
            print(f"\nPatient '{discharged_patient.name}' discharged successfully.")
        else:
            print(f"\nPatient with ID {patient_id} not found.")


hms = HospitalManagementSystem()

hms.add_patient("P001", "Benigne Ngerituje", 24, "Female", "Teeth cavity")
hms.add_patient("P002", "Allelua Niyonzima", 25, "Female", "Headache")

while True:
    print("\n==============================")
    print(" Hospital Management System ")
    print("==============================")
    print("1. Add New Patient")
    print("2. Display All Patients")
    print("3. Search Patient by ID")
    print("4. Discharge Patient")
    print("5. Exit")

    choice = input("\nEnter your choice(1-5): ").strip()

    if choice == '1':
        p_id = input("Enter Patient ID: ").strip()
        name = input("Enter Name: ").strip()
        try:
            age = int(input("Enter Age: ").strip())
        except ValueError:
            print("Invalid age. Please enter a number.")
            continue
        gender = input("Enter Gender: ").strip()
        disease = input("Enter Disease: ").strip()
        hms.add_patient(p_id, name,age,gender, disease)
    elif choice == "2":
        hms.display_patients()

    elif choice == "3":
        p_id = input("Enter Patient ID to search: ").strip()
        hms.search_patient(p_id)

    elif choice == '4':
        p_id = input("Enter Patient ID to discharge: ").strip()
        hms.discharge_patient(p_id)

    elif choice == '5':
        print("\n Thank you for using the Hospital Managemet. Goodbye!!!!")
        break
    else:
        print("\n Invalid option. Please Select between 1 and 5.")
        