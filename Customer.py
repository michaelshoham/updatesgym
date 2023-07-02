from Entity import GymMember
class Customer(GymMember):
    def __init__(self, member_id, name, age, gender, customer_id, payment_plan):
        super().__init__(member_id, name, age, gender)
        self._customer_id = customer_id
        self._payment_plan = payment_plan

    @property
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def payment_plan(self):
        return self._payment_plan
    @payment_plan.setter
    def payment_plan(self, payment_plan):
        self._payment_plan = payment_plan




