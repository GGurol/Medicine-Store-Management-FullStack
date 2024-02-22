from django import forms
from .models import Order, Medicine, OrderedMedicine, Doctor, Patient, Medicine

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['patient', 'status']

        medicine = forms.ModelMultipleChoiceField(queryset=Medicine.objects.all(), widget=forms.CheckboxSelectMultiple)


class OrderedMedicineForm(forms.ModelForm):

    class Meta:
        model = OrderedMedicine
        fields = '__all__'

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'

class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = '__all__'