from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def patienthomepage(request):
    return render(request, 'patientapp/patienthomepage.html')


def logout_view(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('home')


from django.shortcuts import render
from staffapp.models import Appointment, MedicalRecord
from django.contrib.auth.decorators import login_required

@login_required
def patient_appointments_view(request):
    patient = request.user  # Get the logged-in patient
    appointments = Appointment.objects.filter(patient=patient)  # Fetch appointments for this patient
    return render(request, 'patientapp/patient_appointments.html', {'appointments': appointments})

@login_required
def patient_medical_records_view(request):
    patient = request.user
    medical_records = MedicalRecord.objects.filter(patient=patient)
    return render(request, 'patientapp/patient_medical_records.html', {'medical_records': medical_records})

from django.shortcuts import render

from django.shortcuts import render
from django import forms


# BMI Calculation Form
class BMIForm(forms.Form):
    height = forms.FloatField(label='Height (in meters)', min_value=0.1)
    weight = forms.FloatField(label='Weight (in kilograms)', min_value=0.1)


def bmi_view(request):
    bmi = None
    category = None

    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bmi = weight / (height ** 2)

            # Determine BMI category
            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 24.9:
                category = 'Normal weight'
            elif 25 <= bmi < 29.9:
                category = 'Overweight'
            else:
                category = 'Obesity'

        return render(request, 'patientapp/bmi.html', {'form': form, 'bmi': bmi, 'category': category})

    else:
        form = BMIForm()

    return render(request, 'patientapp/bmi.html', {'form': form})

def medicine_info(request):
    return render(request, 'patientapp/medicine_info.html')


from django.shortcuts import render
from staffapp.models import Appointment, MedicalRecord
from django.contrib.auth.decorators import login_required

@login_required
def patient_appointments_view(request):
    patient = request.user  # Get the logged-in patient
    appointments = Appointment.objects.filter(patient=patient)  # Fetch appointments for this patient
    return render(request, 'patientapp/patient_appointments.html', {'appointments': appointments})

def chatbot_view(request):
    return render(request, 'patientapp/chatbot.html')

def book_lab_test(request):
    return render(request, 'patientapp/book_lab_test.html')