from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.UserLoginPageCall, name='login'),  # Updated to 'login'
    path('login/logic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('register/', views.UserRegisterPageCall, name='register_page'),
    path('register/logic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('staffapp/', include(('staffapp.urls', 'staffapp'))),
    path('patientapp/', include(('patientapp.urls', 'patientapp'))),
]
