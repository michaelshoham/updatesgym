from RegularCustomer import RegularCustomer
from PremiumCustomer import PremiumCustomer
from MedicalCustomer import MedicalCustomer


class Payment:
    def calculate_fee(self, customer):
        if isinstance(customer, RegularCustomer):
            return 50
        elif isinstance(customer, PremiumCustomer):
            return 100
        elif isinstance(customer, MedicalCustomer):
            return 200

    def calculate_discount(self, customer):
        if isinstance(customer, MedicalCustomer):
            total_insurance_amount = (self.calculate_fee(customer)
                                      * customer.medical_insurance_amount) / 100
            return self.calculate_fee(customer) - total_insurance_amount

    def generate_invoice(self, customer):
        if isinstance(customer, MedicalCustomer):
            fee = self.calculate_discount(customer)
        else:
            fee = self.calculate_fee(customer)

        invoice = f"Invoice for Customer {customer.name}\nPayment Plan: {customer.payment_plan}\nFee: {fee} USD"
        return invoice
