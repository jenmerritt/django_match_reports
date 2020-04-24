from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'
    ordering = ['-date']

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
