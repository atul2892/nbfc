from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about/', views.aboutPage),
    path('register/', views.registerPage),
    path('bank-register/', views.bankregisterPage),
    path('condidate-register/', views.condidateregisterPage),
    path('registration-thanks/', views.registrationThanksPage),
    path('login/', views.loginPage),
    path('logout/',views.logoutLogic),
    path('loan/', views.loanPage),
    path('bank/<int:id>', views.bankPage),
    path('loan-enquiry/', views.loanEnquiryPage),
    
    
    # ========= Bank Panel Start ==========
    path('bank-dashboard/',views.bank_dashboard),
    path('loan-enquiry-status/<int:id>/<str:ops>/',views.loan_enquiry_status),
    
    
    # ========= Candidate Panel Start ==========
    path('candidate-dashboard/',views.candidate_dashboard),
    # path('loan-enquiry-status/<int:id>/<str:ops>/',views.loan_enquiry_status),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
