from django.urls import path
from staffapp import views



app_name = 'staffapp'

urlpatterns = [
    path('', views.staffhomepage, name='staffhomepage'),
    path('appointments/', views.appointments_view, name='appointments'),
    path('add_appointment/', views.appointments_view, name='add_appointment'),
    path('medical_records/', views.medical_records_view, name='medical_records'),
    path('add_medical_record/', views.medical_records_view, name='add_medical_record'),
    path('logout/', views.logout_view, name='logout'),
    path('register_patient/', views.register_patient, name='register_patient'),
    path('add_staff/', views.add_staff_view, name='add_staff'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('delete_medical_record/<int:record_id>/', views.delete_medical_record, name='delete_medical_record'),
    path('staff_list/', views.staff_list_view, name='staff_list'),
    path('patient_list/', views.patient_list_view, name='patient_list'),
    path('send_sms/', views.send_sms, name='send_sms'),
]
