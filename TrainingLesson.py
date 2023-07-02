from PremiumCustomer import PremiumCustomer
from RegularCustomer import RegularCustomer
from MedicalCustomer import MedicalCustomer
class TrainingLesson:
    def __init__(self, lesson_id, name, time, capacity, coach):
        self._lesson_id = lesson_id
        self._name = name
        self._time = time
        self._capacity = capacity
        self._coach = coach
        self._enrolled_customers = []

    @property
    def lesson_id(self):
        return self._lesson_id
    @lesson_id.setter
    def lesson_id(self, lesson_id):
        self._lesson_id = lesson_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, time):
        self._time = time

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def coach(self):
        return self._coach
    @coach.setter
    def coach(self, coach):
        self._coach = coach
    def equipment_used(self, equipment):
        if equipment.availability:
            print(f"Equipment {equipment.name} is used in the {self.name} lesson.")
            equipment.availability = False
    def enroll_customer(self, customer):
        if isinstance(customer, PremiumCustomer):
            if len(self._enrolled_customers) < self._capacity:
                self._enrolled_customers.append(customer)
                print(f"Customer {customer.name} enrolled in the {self.name} lesson.")
            else:
                print(f"The {self.name} lesson is already full. Customer {customer.name} cannot enroll.")
        elif isinstance(customer, RegularCustomer):
            print(customer.additional_features)
        elif isinstance(customer, MedicalCustomer):
            if len(self._enrolled_customers) < self._capacity:
                self._enrolled_customers.append(customer)
                print(f"Customer {customer.name} enrolled in the {self.name} lesson.")
            else:
                print(f"The {self.name} lesson is already full. Customer {customer.name} cannot enroll.")


    def display_details(self):
        print(f"Lesson: {self.name}")
        print(f"Time: {self.time}")
        print(f"Coach: {self.coach}")
        print(f"Capacity: {len(self._enrolled_customers)}/{self.capacity}")
        print("Enrolled Customers:")
        for customer in self._enrolled_customers:
            print(f"- {customer.name}")
