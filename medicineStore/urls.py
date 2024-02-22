from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine-details/<int:id>', views.medicine_details, name='medicine_details'),
    path('medicine-search/', views.search_medicines, name='search_medicines'),
    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('doctor-profile/<int:id>', views.doctor_profile, name='doctor_profile'),
    path('patient-list/', views.patient_list, name='patient_list'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('patient-profile/<int:id>', views.patient_profile, name='patient_profile'),
    path('view-prescriptions/<int:id>', views.view_prescriptions, name='view_prescriptions'),
    path('view_prescription_details/<int:id>', views.view_prescription_details, name='view_prescription_details'),
    path('create-order/', views.create_order, name='create_order'),
    path('add-order-details/', views.add_order_details, name='add_order_details'),
    path('order-details/<int:id>', views.order_details, name='order_details'),
]