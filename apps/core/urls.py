from django.urls import path
from . import views as v
from .views import *

app_name = 'core'

urlpatterns = [
    path('login/', v.custom_login, name='login'),
    path('create-user/', UserCreateView.as_view(), name='create_user'),
    path('create-user-success/', UserCreateSuccessView.as_view(), name='create_user_success'),
    path('change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('change-password-success/', PasswordChangeSuccessView.as_view(), name='change_password_success'),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password-success/', PasswordResetSuccessView.as_view(), name='reset_password_success'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('switch-tenant/', TenantSwitchView.as_view(), name='switch_tenant'),  # Add this line
    

]

