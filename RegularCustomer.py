from Customer import Customer
class RegularCustomer(Customer):
    def __init__(self, member_id, name, age, gender, customer_id, payment_plan, additional_features):
        super().__init__(member_id, name, age, gender, customer_id, payment_plan)
        self._additional_features = additional_features

    @property
    def additional_features(self):
        if self._additional_features == 'Self training':
            self._additional_features = 'Self training'
        return f"Cutomer {self._name} is not allowed to use {self._additional_features} " \
               f"\nupgrade to Premium Customer to use all features"
    @additional_features.setter
    def additional_features(self, additional_features):
        self._additional_features = additional_features