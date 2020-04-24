from django.shortcuts import render
from django.views.generic import ListView
from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'
    ordering = ['-date']

# def index(request):
    # return render(request, "reports/report_list.html", locals())