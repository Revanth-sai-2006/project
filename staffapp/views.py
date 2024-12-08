from django.shortcuts import render, redirect
from .models import MedicalRecord, Appointment
from .forms import AppointmentForm, MedicalRecordForm
from django.contrib.auth.decorators import login_required

@login_required
def staffhomepage(request):
    return render(request, 'staffapp/staffhomepage.html')


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

@login_required
def appointments_view(request):
    appointments = Appointment.objects.all()
    form = AppointmentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Save the appointment
        appointment = form.save()

        # Send an email to the patient after the appointment is saved
        patient_email = appointment.patient.email  # Get patient's email from the User model

        # Compose the email
        subject = 'Appointment Confirmation'
        message = f"Dear {appointment.patient.username},\n\nYour appointment with Dr. {appointment.doctor.username} is confirmed for {appointment.date} at {appointment.time}.\n\nReason for visit: {appointment.reason}\n\nThank you."
        from_email = settings.EMAIL_HOST_USER  # Sender's email (configured in settings)

        # Send the email
        try:
            send_mail(subject, message, from_email, [patient_email])
            messages.success(request, 'Appointment added and confirmation email sent to the patient.')
        except Exception as e:
            messages.error(request, f"Error sending email: {str(e)}")

        return redirect('staffapp:appointments')

    return render(request, 'staffapp/appointments_view.html', {'appointments': appointments, 'form': form})

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MedicalRecordForm
from .models import MedicalRecord

@login_required
def medical_records_view(request):
    records = MedicalRecord.objects.all()
    form = MedicalRecordForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Save the medical record
        medical_record = form.save()

        patient_email = medical_record.patient.email  # Get patient's email from the User model

        # Compose the email
        subject = 'New Medical Record Created'
        message = f"Dear {medical_record.patient.username},\n\nA new medical record has been created for you by Dr. {medical_record.doctor.username}.\n\nDetails:\n{medical_record.description}\n\nDate: {medical_record.date}\n\nThank you."
        from_email = settings.EMAIL_HOST_USER  # Sender's email (configured in settings)

        # Send the email
        try:
            send_mail(subject, message, from_email, [patient_email])
            messages.success(request, 'Medical record added and confirmation email sent to the patient.')
        except Exception as e:
            messages.error(request, f"Error sending email: {str(e)}")

        return redirect('staffapp:medical_records')

    return render(request, 'staffapp/medical_records_view.html', {'records': records, 'form': form})

def logout_view(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('home')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientRegistrationForm
from django.contrib.auth.decorators import login_required


@login_required
def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)

        # Check if the form is valid or not
        if form.is_valid():
            form.save()  # Save the patient (User) to the database
            messages.success(request, 'Patient has been successfully registered.')
            return redirect('staffapp:staffhomepage')  # Redirect after registration
        else:
            # Print the form errors if it's invalid
            print("Form is invalid: ", form.errors)
            messages.error(request, 'There were errors in the form.')
    else:
        form = PatientRegistrationForm()  # Empty form for GET request

    return render(request, 'staffapp/register_patient.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import StaffRegistrationForm

# View for adding new staff
def add_staff_view(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffapp:staffhomepage')
    else:
        form = StaffRegistrationForm()
    return render(request, 'staffapp/add_staff.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('staffapp:appointments')

    return render(request, 'staffapp/confirm_delete.html', {'appointment': appointment})

from django.shortcuts import get_object_or_404
from .models import MedicalRecord
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def delete_medical_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)

    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Medical record deleted successfully!')
        return redirect('staffapp:medical_records')  # Redirect after deletion

    return render(request, 'staffapp/confirm_delete1.html', {'record': record})

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def staff_list_view(request):
    staff_list = User.objects.filter(username__regex=r'^\d{4}$')  # Select users with 4-digit usernames
    return render(request, 'staffapp/staff_list.html', {'staff_list': staff_list})

@login_required
def patient_list_view(request):
    patient_list = User.objects.filter(username__regex=r'^\d{10}$')  # Select users with 10-digit usernames
    return render(request, 'staffapp/patient_list.html', {'patient_list': patient_list})


# staffapp/views.py

from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from django.http import HttpResponse

def send_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        remarks = request.POST.get('remarks')

        # Twilio logic to send SMS (ensure Twilio is correctly configured)
        account_sid = 'AC3990c71de3e5f3840c3bb33f511acfab'
        auth_token = 'bf54493583eae83a5e6b8c26a32931ce'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=remarks,
            from_='+17752966522',
            to=phone_number
        )

        return render(request, 'staffapp/send_sms.html', {'message': 'SMS sent successfully!'})

    return render(request, 'staffapp/send_sms.html')

