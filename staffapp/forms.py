from django import forms
from .models import Appointment, MedicalRecord

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'reason', 'notes']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'description']  # No 'date' field since it's auto-added



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Custom validation for username (e.g., patient ID)
    def clean_username(self):
        username = self.cleaned_data['username']

        # Ensure username is 10 digits (e.g., patient ID)
        if len(username) != 10 or not username.isdigit():
            raise ValidationError("Username must be exactly 10 digits.")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError("This patient ID is already taken.")

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Save email
        user.is_active = True  # Make sure the user is active
        user.is_staff = False  # Ensure they are not a staff member

        if commit:
            user.save()  # Save the user to the auth_user table

        return user


from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isdigit() or len(username) != 4:
            raise ValidationError("Username must be exactly 4 digits.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# forms.py in the Staff app
from django import forms

class SMSForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    remarks = forms.CharField(widget=forms.Textarea, label="Remarks")