from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('login/', views.loginuser, name='loginuser'),
    path('signup/', views.signup, name='signupuser'),
    path('logout-user/', views.logoutuser, name='logoutuser'),
    path('valid-username/', views.validate_username, name='username'),
    path('valid-email/', views.validate_email, name='validemail'),

    # Reset Password path
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(template_name='Account/password_change_form.html'),
        name='reset_password'
    ),

    path(
        'reset-password-send/',
        auth_views.PasswordResetDoneView.as_view(template_name='Account/password_mail_send.html'),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='Account/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),

    path(
        'reset/-password-complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='Account/password_reset_done.html'),
        name='password_reset_complete'
    )
]
