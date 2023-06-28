from GymMemberClass import GymMember
class Customer(GymMember):

    def __init__(self, name, member_id, age, gender, phone_num, email, payment_plan):
        super().__init__(name, member_id, age, gender, phone_num, email)
        self.customer_id = member_id
        self._payment_plan = payment_plan

    @property
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        if customer_id != "":
            self._customer_id = customer_id
        else:
            print("Customer ID cannot be empty!")

    @property
    def payment_plan(self):
        return self._payment_plan
    @payment_plan.setter
    def payment_plan(self, payment_plan):
        if payment_plan != "":
            self._payment_plan = payment_plan
        else:
            print("Payment plan cannot be empty!")

    def print_customer_info(self):
        GymMember.print_member_info(self)
        print(f"Payment plan: {self._payment_plan}")

class RegularCustomer(Customer):

    def __init__(self, name, member_id, age, gender, phone_num, email, payment_plan, services):
        super().__init__(name, member_id, age, gender , phone_num, email, payment_plan)
        self._services = services

    @property
    def services(self):
        return self._services
    @services.setter
    def services(self, services):
        if services != "":
            self._services = services
        else:
            print("Services cannot be empty!")

    def print_regular_customer_info(self):
        print(f"Customer {GymMember.name(self)} is a regular customer. "
              f"\nHe/She has the following services: {self._services}")

class PremiumCustomer(Customer):

    def __init__(self, name, member_id, age, gender, phone_num, email, payment_plan, additional_features):
        super().__init__(name, member_id, age, gender, phone_num, email, payment_plan)
        self._additional_features = additional_features

    @property
    def additional_features(self):
        return self._additional_features
    @additional_features.setter
    def additional_features(self, additional_features):
        if additional_features != "":
            self._additional_features = additional_features
        else:
            print("Additional features cannot be empty!")

    def print_premium_customer_info(self):
        print(f"Customer {GymMember.name(self)} is a premium customer."
              f"\nHe/She has the following additional features: {self._additional_features}")
