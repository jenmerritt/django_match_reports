from django.urls import path
from . import views
from .views import ReportListView, ReportDetailView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", ReportListView.as_view(), name='reports-home'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]