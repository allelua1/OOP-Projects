from appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []
        self.appointment_counter = 1

    def add_doctor(self,doctor):
        self.doctors.append(doctor)
        print(f"Dr. {doctor.name} added successfully.")

    def find_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def list_doctors(self):
        if not self.doctors:
            print("No doctors registered.")
            return
        print(f"\n{'='*40}")
        print(f"   DOCTORS IN  {self.name.upper()}")
        print(f"{'='*40}")
        for doctor in self.doctors:
            print(f" {doctor.doctor_id} | Dr. {doctor.name} | {doctor.specialization}")
        print(f"{'='*40}")

    # patient methods
    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} registered  successfully.")

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None
    def list_patient(self):
        if not self.patients:
            print("No patients registered.")
        print(f"\n{'='*40}")
        print("      REGISTERED PATIENTS ")
        print(f"{'='*40}")
        for patient in self.patients:
            print(f" {patient.patient_id} | {patient.name} | {patient.blood_group}")

    # Appointment methods
    def book_appointment(self, patient_id, doctor_id, date, time, reason):
        # book new appointment

        patient = self.find_patient(patient_id)
        doctor = self.find_doctor(doctor_id)

        if not patient:
            print(f"Patient ID '{patient_id}' not found.")
            return
        if not doctor:
            print(f"Doctor ID '{doctor_id}' not found.")

        # generate appointment id
        apt_id = f"APT{self.appointment_counter:03d}"
        self.appointment_counter += 1

        appointment = Appointment(apt_id, patient, doctor, date, time, reason)
        self.appointments.append(appointment)

        print(f"\n Appointment booked successfully!")
        print(f" ID : {apt_id}")
        print(f"Patient : {patient.name}")
        print(f" Doctor : Dr. {doctor.name}")
        print(f" Date : {date} at {time}")

    def cancel_appointment(self, appointment_id) :
        appointment = self.find_appointment(appointment_id)
        if appointment:
            appointment.cancel()
        else:
            print(f"Appointment '{appointment_id}'not found.")
    def list_appointment(self):
        if not self.appointments:
            print("No appointments found.")
            return
        print(f"{'='*60}")
        print("ALL APPOINTMENT")
        print(f"{'='*60}")
        for apt in self.appointments:
            print(f"{apt}")
        print(f"{'='*60}")

    def list_appointments_by_doctor(self, doctor_id):
        results = [a for a in self.appointments if a.doctor.doctor_id == doctor_id]
        if not results:
            print("No appointments found for this doctor.")
            return
        print(f"\n--- Appointments for Dr. {results[0].doctor.name} ----")
        for apt in results:
            print(f" {apt}")

    def list_appointments_by_patient(self, patient_id):
        results = [a for a in self.appointments if a.patient.patient_id == patient_id]
        if not results:
            print("No appointments found for this patient.")
            return
        print(f"\n--- Appointments for {results[0].patient.name} ---")
        for apt in results:
            print(f" {apt}")

    def find_appointment(self, appointment_id):
        for apt in self.appointments:
            if apt.appointment_id == appointment_id:
                return apt
        return None