from django.contrib import admin
from .models import Patient, Doctor, Medicine, Prescription, PrescribedMedicine, Order, OrderedMedicine

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(PrescribedMedicine)
admin.site.register(Order)
admin.site.register(OrderedMedicine)
