from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient, Medicine, Prescription, PrescribedMedicine, Order, OrderedMedicine
from django.db.models import Q
from .forms import OrderForm, OrderedMedicineForm, DoctorForm, PatientForm, MedicineForm
from django.contrib import messages


# Create your views here.
def home(request):
    latest_medicines = Medicine.objects.all().order_by('-id')[:8]
    context = {'latest_medicines': latest_medicines}
    return render(request, 'home.html', context)

def search_medicines(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        results = Medicine.objects.filter(
            Q(name__icontains=search_term) | Q(generic_name__icontains=search_term)
        ).order_by('name')
        context = {'results': results, 'search_term': search_term}
        return render(request, 'medicine_search_results.html', context)
    else:
        return render(request, 'medicine_search.html')

def medicine_details(request, id):
    try:
        medicine = Medicine.objects.get(id=id)
        context = {'medicine': medicine}
        return render(request, 'medicine_details.html', context)
    except Medicine.DoesNotExist:
        return redirect('search_medicines')
    
    

def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor_list.html', context)

def doctor_profile(request, id):
    doctor = Doctor.objects.get(id=id)
    context = {'doctor': doctor}
    return render(request, 'doctor_profile.html', context)

def patient_list(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient_list.html', context)

def patient_profile(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'patient_profile.html', context)


def view_prescriptions(request, id):
    patient = Patient.objects.get(id=id)
    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date_prescribed')
    context = {'prescriptions': prescriptions}
    return render(request, 'prescription_list.html', context)


def view_prescription_details(request, id):
    patient = Patient.objects.get(prescription__id=id)
    try:
        prescription = Prescription.objects.get(id=id, patient=patient)
        prescribed_medicines = PrescribedMedicine.objects.filter(prescription=prescription)
        context = {'prescription': prescription, 'prescribed_medicines': prescribed_medicines}
        return render(request, 'prescription_details.html', context)
    except Prescription.DoesNotExist:
        return redirect('view_prescriptions')
    

def create_order(request):
    order_form = OrderForm()
    if request.method=='POST':
        order_form = OrderForm(request.POST)
        order_form.save()
        return redirect('add_order_details')
    return render(request, 'create_order.html', {'form': order_form})

def add_order_details(request):
    ordered_medicine_form = OrderedMedicineForm()
    if request.method=='POST':
        ordered_medicine_form = OrderedMedicineForm(request.POST)
        ordered_medicine_form.save()
        return redirect('home')

    return render(request, 'add_order_details.html', {'form': ordered_medicine_form})


def order_details(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return redirect('error_page')

    context = {
        'order': order,
    }

    return render(request, 'order_details.html', context)


def add_doctor(request):
    frm = DoctorForm()
    if request.method=='POST':
        frm = DoctorForm(request.POST)
        frm.save()
        return redirect('doctor_list')

    return render(request, 'add_doctor.html', {'form': frm})

def add_patient(request):
    frm = PatientForm()
    if request.method=='POST':
        frm = PatientForm(request.POST)
        frm.save()
        return redirect('patient_list')

    return render(request, 'add_patient.html', {'form': frm})

def add_medicine(request):
    frm = MedicineForm()
    if request.method=='POST':
        frm = MedicineForm(request.POST)
        frm.save()
        return redirect('home')

    return render(request, 'add_medicine.html', {'form': frm})
