from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from ..models import Employee, Customer, Product, Complaint
from ..forms import ComplaintForm, EmployeeForm, ProductForm, CustomerForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class AdminDashboardView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = "admin/dashboard.html"


class EmployeeListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Employee
    template_name = "admin/employee_list.html"
    context_object_name = "employees"

class EmployeeCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'admin/employee_form.html'
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        username = form.cleaned_data.pop('username')
        password = form.cleaned_data.pop('password')
        email = form.cleaned_data['email']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=False,
            role=User.Role.EMPLOYEE
        )

        form.instance.user = user
        return super().form_valid(form)

class EmployeeUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'admin/employee_form.html'
    success_url = reverse_lazy('employee_list')

# --- Customer Views ---
class CustomerListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Customer
    template_name = 'admin/customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'admin/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'admin/customer_form.html'
    success_url = reverse_lazy('customer_list')


# --- Product Views ---
class ProductListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Product
    template_name = 'admin/product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/product_form.html'
    success_url = reverse_lazy('product_list')

class ComplaintListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Complaint
    template_name = "admin/complaint_list.html"
    context_object_name = "complaints"

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Complaint.ComplaintStatus.choices
        context['selected_status'] = self.request.GET.get('status', '')
        return context

class ComplaintCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = "admin/complaint_form.html"
    success_url = reverse_lazy("complaint_list")

class AdminComplaintUpdateView(UpdateView):
    model = Complaint
    fields = "__all__"
    template_name = "admin/complaint_form.html"
    success_url = reverse_lazy('complaint_list')
