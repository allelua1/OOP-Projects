class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, reason):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.reason = reason
        self.status = "Scheduled"
        self.notes = " "
        self.fees_paid = False

    def cancel(self):
        if self.status == "Scheduled":
            self.status = "Cancelled"
            print(f"Appointment {self.appointment_id} has been cancelled.")

        else:
            print(f"Can not cancel. Current status: {self.status}")

    def complete(self, notes=""):
        self.status = "Completed"
        self.notes = notes
        self.fees_paid = True
        print(f"Appointment {self.appointment_id} marked as completed.")
    def reschedule(self, new_date, new_time):
        if self.status == "Cancelled":
            print("Cannot reschedule a canceled appointment.")
        else:
            self.date = new_date
            self.time = new_time
            self.status = "Rescheduled"
            print(f"Appointment rescheduled to {new_date} at {new_time}.")

    def get_details(self):
        return (
            f"Appointment ID : {self.appointment_id}\n"
            f"Patient : {self.patient.name}\n"
            f"Doctor : Dr. {self.doctor.name}\n"
            f"Specialization : {self.doctor.specialization}\n"
            f"Date : {self.date}\n"
            f"Time : {self.time}\n"
            f"Reason : {self.reason}\n"
            f"Status : {self.status}\n"
            f"Fee Paid : {'Yes' if self.self.fees_paid else 'No'}\n"
            f"Notes : {self.notes if self.notes else 'None'}"
        )
    def __str__(self):
        return (f"[{self.appointment_id}] {self.patient.name} "
                f"-> Dr. {self.doctor.name} on {self.date}"
                f"at {self.time} [{self.status}]")
        