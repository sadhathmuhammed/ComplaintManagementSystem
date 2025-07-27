from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from ..models import Complaint, Employee
from ..forms import ComplaintUpdateForm
from django.shortcuts import redirect, get_object_or_404
from django.views import View

class EmployeeRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_staff

class EmployeeDashboardView(LoginRequiredMixin, EmployeeRequiredMixin, TemplateView):
    template_name = "employee/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.request.user.employee_profile
        context['assigned_count'] = Complaint.objects.filter(assigned_employee=employee).count()
        context['unassigned_count'] = Complaint.objects.filter(assigned_employee__isnull=True).count()
        return context


class AssignedComplaintsView(LoginRequiredMixin, EmployeeRequiredMixin, ListView):
    model = Complaint
    template_name = "employee/assigned_complaints.html"
    context_object_name = "complaints"

    def get_queryset(self):
        return Complaint.objects.filter(assigned_employee=self.request.user.employee_profile)


class UnassignedComplaintsView(LoginRequiredMixin, EmployeeRequiredMixin, ListView):
    model = Complaint
    template_name = "employee/unassigned_complaints.html"
    context_object_name = "complaints"

    def get_queryset(self):
        return Complaint.objects.filter(assigned_employee__isnull=True)


class AssignToMeView(View):
    def post(self, request, pk):
        # Get the logged-in employee
        employee = get_object_or_404(Employee, user=request.user)

        # Find the complaint and assign it
        complaint = get_object_or_404(Complaint, pk=pk, assigned_employee__isnull=True)
        complaint.assigned_employee = employee
        complaint.save()

        return redirect('unassigned_complaints')

class ComplaintUpdateView(LoginRequiredMixin, EmployeeRequiredMixin, UpdateView):
    model = Complaint
    form_class = ComplaintUpdateForm
    template_name = "employee/update_complaint.html"
    success_url = reverse_lazy("assigned_complaints")

    def form_valid(self, form):
        complaint = form.save(commit=False)
        if 'assign_me' in self.request.POST and not complaint.assigned_employee:
            complaint.assigned_employee = self.request.user.employee_profile
        complaint.save()
        return super().form_valid(form)
