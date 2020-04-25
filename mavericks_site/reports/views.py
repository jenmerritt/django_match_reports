from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
    ordering = ['-date']
    paginate_by = 3

# def index(request):
    # return render(request, "reports/report_list.html", locals())

class ReportDetailView(DetailView):
    model = Report

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    fields = ['title', 'content', 'date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.author:
            return True
        return False


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    success_url = '/'

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.author:
            return True
        return False
    
class UserReportListView(ListView):
    model = Report
    template_name = 'reports/user_reports.html'
    context_object_name = 'reports'
    ordering = ['-date']
    # get the user
    def get_queryset(self):
        # if the user exists, capture them else display a 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # filter posts by the user tha it's grabbed
        return Report.objects.filter(author=user).order_by('-date')
    
    def get_template_names(self):
        return ["reports/user_report_list.html"]
