from Customer import Customer

class MedicalCustomer(Customer):

    def __init__(self, member_id, name, age, gender, customer_id, payment_plan, medical_disability):
        super().__init__(member_id, name, age, gender, customer_id, payment_plan)
        self._medical_disability = medical_disability
        self._medical_insurance = None
        self._medical_insurance_amount = None
        self._medical_insurance_company = None

    @property
    def medical_disability(self):
        return self._medical_disability
    @medical_disability.setter
    def medical_disability(self, medical_disability):
        self._medical_disability = medical_disability

    @property
    def medical_insurance(self):
        return self._medical_insurance
    @medical_insurance.setter
    def medical_insurance(self, medical_insurance):
        self._medical_insurance = medical_insurance

    @property
    def medical_insurance_amount(self):
        return self._medical_insurance_amount
    @medical_insurance_amount.setter
    def medical_insurance_amount(self, medical_insurance_amount):
        self._medical_insurance_amount = medical_insurance_amount

    @property
    def medical_insurance_company(self):
        return self._medical_insurance_company
    @medical_insurance_company.setter
    def medical_insurance_company(self, medical_insurance_company):
        self._medical_insurance_company = medical_insurance_company
