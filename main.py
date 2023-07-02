from RegularCustomer import RegularCustomer
from PremiumCustomer import PremiumCustomer
from MedicalCustomer import MedicalCustomer
from Trainer import Trainer
from Payment import Payment
from TrainingLesson import TrainingLesson
from FitnessEquipment import FitnessEquipment

def main():
    # Creating customers and trainers
    customer1 = RegularCustomer("001", "John Doe", 25, "Male", "C001", "Regular", ["Weights"])
    customer2 = PremiumCustomer("002", "Jane Smith", 30, "Female", "C002", "Premium", ["Weights", "Yoga"])
    customer3 = MedicalCustomer("003", "Ahmad Tibi", 50, "Male", "C003", "Medical", ["Hydrotherapy", "Gross motor skill"])
    trainer1 = Trainer("T001", "Mike Johnson", 35, "Male", "Trainer001", "Weightlifting")
    trainer2 = Trainer("T002", "Tony Cohen", 30, "Male", "Trainer002", "Yoga")
    trainer2.medical_certification = 'YES'

    customer3.medical_insurance_amount = 80

    # Creating fitness equipment
    equipment1 = FitnessEquipment("E001", "Treadmill")
    equipment2 = FitnessEquipment("E002", "Dumbbells")

    # Creating training lessons
    lesson1 = TrainingLesson("L001", "Weightlifting Class", "10:00 AM - 11:00 AM", 5, trainer1.name)
    lesson2 = TrainingLesson("L002", "Yoga Class", "4:00 PM - 5:00 PM", 10, trainer1.name)
    lesson3 = TrainingLesson("L003", "Hydrotherapy Class", "4:00 PM - 5:00 PM", 10, trainer2.name)

    # Enrolling customers in training lessons
    lesson1.enroll_customer(customer1)
    lesson1.enroll_customer(customer2)
    lesson2.enroll_customer(customer2)
    lesson3.enroll_customer(customer3)

    # Displaying lesson details
    lesson1.display_details()
    lesson2.display_details()
    lesson3.display_details()

    # Checking equipment availability
    print(f"Equipment {equipment1.name} availability: {equipment1.availability}")
    print(f"Equipment {equipment2.name} availability: {equipment2.availability}")

    #equipment used in lesson
    lesson1.equipment_used(equipment1)



    # Checking updated equipment availability
    print(f"Equipment {equipment1.name} availability: {equipment1.availability}")
    print(f"Equipment {equipment2.name} availability: {equipment2.availability}")

    # Calculating and generating invoice
    payment = Payment()
    invoice = payment.generate_invoice(customer1)
    medical_invoice = payment.generate_invoice(customer3)
    print(invoice)
    print(medical_invoice)

if __name__ == "__main__":
    main()
