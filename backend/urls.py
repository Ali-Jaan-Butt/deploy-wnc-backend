"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from backend_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.check_backend),
    path("admin/", admin.site.urls),
    path('api/recieve-signup-data/', views.receive_signup_data, name='receive_signup_data'),
    path('api/recieve-student-data/', views.receive_student_data, name='receive_student_data'),
    path('api/recieve-supervisor-data/', views.receive_supervisor_data, name='receive_supervisor_data'),
    path('api/recieve-company-data/', views.receive_company_data, name='receive_company_data'),
    path('api/get-signup-data/', views.get_signup_data, name='get-data'),
    path('api/get-student-data/', views.get_student_data, name='get-student-data'),
    path('api/get-supervisor-data/', views.get_supervisor_data, name='get-supervisor-data'),
    path('api/get-company-data/', views.get_company_data, name='get-company-data'),
    path('ver/email/', views.receive_verify_email, name='verify-email'),
    path('sup/profile-data/', views.recieve_sup_profile, name='recieve_sup_data'),
    path('quiz-data/user-test/', views.quiz_data, name='quiz_data'),
    path('receive-job-posting/', views.receive_post_job, name='receive_job_posting'),
    path('get-job-posting/', views.get_jobs, name='get_jobs'),
    path('receive-proposal-posting/', views.receive_proposal, name='receive_proposal'),
    path('get-proposal-posting/', views.get_proposal, name='get_proposals'),
    path('receive-place-order-posting/', views.place_order, name='place_order'),
    path('get-place-order-posting/', views.get_orders, name='get_orders'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
