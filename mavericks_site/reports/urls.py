from django.urls import path
from . import views
from .views import ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView, UserReportListView

urlpatterns = [
    path("", ReportListView.as_view(), name='reports-home'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('user/<str:username>/', UserReportListView.as_view(), name='user-reports'),
]