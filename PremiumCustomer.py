from Customer import Customer
class PremiumCustomer(Customer):
    def __init__(self, member_id, name, age, gender, customer_id, payment_plan, additional_features):
        super().__init__(member_id, name, age, gender, customer_id, payment_plan)
        self._additional_features = additional_features

    @property
    def additional_features(self):
        return self._additional_features
    @additional_features.setter
    def additional_features(self, additional_features):
        self._additional_features = additional_features
