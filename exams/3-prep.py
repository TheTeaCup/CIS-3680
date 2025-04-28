# Final Exam Prep
import datetime

class Loan:
    def __init__(self):
        self.id = "1212"
        self.agent = "Micky Da Shark"
        self.amount = 1000.00
        self.rate = .20
        self.customer = None
    
    def __str__(self):
        return f"Loan {self.id} by {self.agent} for {self.amount} (Rate: {self.rate}) to {self.customer}"

class Customer:
    def __init__(self, id, first_name, last_name, email, phone, birth_date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_age()} years old)"

    def get_age(self):
        """Returns customer age in years"""
        today = datetime.date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def is_eligible(self):
        """Returns True if customer is 21 or older, False otherwise"""
        if self.get_age() >= 21:
            return True
        else:
            return False


def main():
    """Test program for Loan and Customer classes"""
    print("Please enter the customer information.")

    id = input("Customer Id: ")
    first_name = input("Firstname: ")
    last_name = input("Lastname: ")
    email = input("Email: ")
    phone = input("Phone: ")
    dob_str = input("Date of Birth (mm/dd/yyyy): ")
    
    birth_date = datetime.datetime.strptime(dob_str, '%m/%d/%Y').date()

    customer = Customer(id, first_name, last_name, email, phone, birth_date)
    loan = Loan()

    if customer.is_eligible():
        loan.customer = customer
        print(loan)
    else:
        print("Customer is not eligible for loan.")


if __name__ == '__main__':
    main()
