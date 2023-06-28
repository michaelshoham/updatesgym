from GymMemberClass import GymMember
class Trainer(GymMember):

    def __init__(self, name, member_id, age, gender, phone_num, email, expertise):
        super().__init__(name, member_id, age, gender, phone_num, email)
        self.trainer_id = member_id
        self._expertise = expertise

    @property
    def trainer_id(self):
        return self._trainer_id
    @trainer_id.setter
    def trainer_id(self, trainer_id):
        if trainer_id != "":
            self._trainer_id = trainer_id
        else:
            print("Trainer ID cannot be empty!")

    @property
    def expertise(self):
        return self._expertise
    @expertise.setter
    def expertise(self, expertise):
        if expertise != "":
            self._expertise = expertise
        else:
            print("Expertise cannot be empty!")

    def print_trainer_info(self):
        GymMember.print_member_info(self)
        print(f"Trainer expertise: {self._expertise}")
