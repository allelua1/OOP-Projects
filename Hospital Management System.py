""" import datetime
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
         """

from hospital import Hospital
from doctor import Doctor
from patient import Patient
from datetime import date

# initialize Hospita
hospital = Hospital("Nairobi General Hospital")

doc1 = Doctor("PER001", "Benigne Ngerituje", 24, "Female",
              "8977778898", "benigne@gmail.com", "Nairobi",
              "D001", "Cardiologist", "Cardiology", 
              "MD,MBBS", 15, ["MON", "WED", "FRI"], 30000)

doc2 = Doctor ("PER002", "Diane Tuyishimire", 24, "Male",
              "8977778898", "benigne@gmail.com", "Nairobi",
              "D001", "Pediatrician", "padriatrics", 
              "MBBS", 10, ["TUE", "THU", "SAT"], 250000)

pat1 = Patient("PER003", "Brian Otieno", 29, "Male",
               "0722000001", "brian@gmail.com", "Kisumu",
               "PT001", "O+", ["Asthma"], ["Penicillin"],
               "0733000001", "INS001", "2024-01-10")

pat2 = Patient("PER004", "Grace Wanjiru", 34, "Female",
               "0722000002", "grace@gmail.com", "Nairobi",
               "PT002", "A+", [], [],
               "0733000002", "INS002", "2024-01-15")

hospital.add_doctor(doc1)
hospital.add_doctor(doc2)
hospital.add_patient(pat1)
hospital.add_patient(pat2)


while True:
        print(f"\n{'='*40}")
        print(f" {hospital.name.upper()}")
        print(f"\n{'='*40}")
        print("1. Doctors Menu")
        print(" 2. Patient Menu")
        print("3. Appointment Menu")
        print("0. Exit")
        print(f"\n{'='*40}")

        choice = input("Enter choice: ")

        if choice == "1":
            hospital.list_patient()
            hospital.list_doctors()
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            date = input("Enter Date (YYY-MM-DD): ")
            time = input("Enter Time(e.g 10:30 AM): ")
            reason = input("Enter Reason: ")

            hospital.book_appointment(patient_id, doctor_id, date, time, reason)

        elif choice == "2":
            hospital.list_appointment()
            apt_id = input("Enter Appointment ID to cancel: ")
            hospital.cancel_appointment(apt_id)

        elif choice == "3":
            hospital.list_appointment()

        elif choice == "4":
            hospital.list_doctors()
            doc_id = input("Enter Doctor ID: ")
            hospital.list_appointments_by_doctor(doc_id)
        elif choice == "5":
            hospital.list_patient()
            pat_id = input("Enter Patient ID: ")
            hospital.list_appointments_by_patient(pat_id)
        elif choice == "0":
            break
    