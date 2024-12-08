from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    notes = models.TextField(blank=True, null=True)  # Optional notes field

    def _str_(self):
        return f"Appointment of {self.patient.username} with {self.doctor.username}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_records")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"Medical Record of {self.patient.username} on {self.date}"