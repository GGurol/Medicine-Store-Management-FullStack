from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='MALE')

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='MALE')

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='prescription')
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    date_prescribed = models.DateField()
    medicines = models.ManyToManyField(Medicine, through='PrescribedMedicine')

    def __str__(self):
        # Access medicines through the PrescribedMedicine intermediary model
        prescribed_medicines = ", ".join([prescribed_medicine.medicine.name for prescribed_medicine in self.prescribedmedicine_set.all()])
        return f"Prescription for {self.patient.name} - Medicines: {prescribed_medicines}"
    
class PrescribedMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicine.name} - {self.dosage} - Quantity: {self.quantity}"
    
class Order(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, through='OrderedMedicine', blank=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return f"Order for {self.patient}"
    
class OrderedMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicine.name} - Quantity: {self.quantity}"