from Entity import GymMember
class Trainer(GymMember):
    def __init__(self, member_id, name, age, gender, trainer_id, expertise):
        super().__init__(member_id, name, age, gender)
        self._trainer_id = trainer_id
        self._expertise = expertise
        self._medical_certification = None

    @property
    def trainer_id(self):
        return self._trainer_id
    @trainer_id.setter
    def trainer_id(self, trainer_id):
        self._trainer_id = trainer_id

    @property
    def expertise(self):
        return self._expertise
    @expertise.setter
    def expertise(self, expertise):
        self._expertise = expertise

    @property
    def medical_certification(self):
        return self._medical_certification
    @medical_certification.setter
    def medical_certification(self, medical_certification):
        if medical_certification == 'YES':
            self._medical_certification = True
        else:
            self._medical_certification = False