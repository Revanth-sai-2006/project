from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminapp.urls')),
    path('staffapp/', include(('staffapp.urls'),namespace='staffapp')),
    path('patientapp/', include(('patientapp.urls'),namespace='patientapp')),
]
