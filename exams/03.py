# CIS 3680 - Assessment #3
import datetime

class Patient:
    # Patient ID, First Name, Last Name, Email, Phone, Date of Birth, Doctor
    def __init__(self, id, first_name, last_name, email, phone, birth_date, doctor):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.doctor = doctor

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_age()} years old)"

    def get_age(self):
        """Returns customer age in years"""
        today = datetime.date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def is_eligible(self):
        """Returns True if customer is 18 or older, False otherwise"""
        if self.get_age() >= 18:
            return True
        else:
            return False

class Doctor:
    # Doctor ID, Name, Specialty, Phone, Email
    def __init__(self):
        self.id = "123456789"
        self.name = "Ed Hassler"
        self.specialty = "Podiatry"
        self.email = "ed.hassler@podiatrist.com"
        self.phone = "828-828-8228"

    def __str__(self):
        return f"Doctor ID: {self.id}\nName: Dr. {self.name}\nSpecialty: {self.specialty}\nEmail: {self.email}\nPhone: {self.phone}"
    
    def get_name(self):
        """returns the doctor's name"""
        return self.name

def main():
    print("Please input patient information")

    id = input("Patient ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    dob_str = input("Date of Birth (mm/dd/yyyy): ")
    doctor_name = input("Patient's Doctor: ")

    birth_date = datetime.datetime.strptime(dob_str, '%m/%d/%Y').date()

    patient = Patient(id, first_name, last_name, email, phone, birth_date, doctor=doctor_name)
    doctor = Doctor()

    if patient.is_eligible():
        if doctor.get_name() == doctor_name:
            print(f"\nPatient is {patient.get_age()} years-old")
            print(doctor)
        else:
            print(f"Invalid Doctor Name. Valid Option(s): {doctor.get_name()}")
    else:
        print("Patient is not 18-years or older.")

if __name__ == '__main__':
    main()
