from django.urls import path
from . import views

app_name = 'patientapp'

urlpatterns = [
    path('', views.patienthomepage, name='patienthomepage'),
    path('appointments/', views.patient_appointments_view, name='patient_appointments'),  # Ensure view name is correct here
    path('medical_records/', views.patient_medical_records_view, name='patient_medical_records'),  # Ensure view name is correct here
    path('logout/', views.logout_view, name='logout'),
    path('bmi/', views.bmi_view, name='bmi'),
    path('medicine-info/', views.medicine_info, name='medicine_info'),
    path('chat/', views.chatbot_view, name='chatbot'),
    path('book_lab_test/', views.book_lab_test, name='book_lab_test'),
]