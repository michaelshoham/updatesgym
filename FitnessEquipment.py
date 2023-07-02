class FitnessEquipment:
    def __init__(self, equipment_id, name):
        self._equipment_id = equipment_id
        self._name = name
        self._availability = True

    @property
    def equipment_id(self):
        return self._equipment_id
    @equipment_id.setter
    def equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def availability(self):
        if not self._availability:
            print("Equipment is currently unavailable.")
        return self._availability
    @availability.setter
    def availability(self, is_available):
        self._availability = is_available