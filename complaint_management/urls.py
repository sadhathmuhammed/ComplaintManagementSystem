from django.urls import path
from .views.admin_views import AdminDashboardView, EmployeeListView, CustomerListView, \
    ProductListView, ComplaintListView, ComplaintCreateView, EmployeeCreateView, \
    EmployeeUpdateView, CustomerCreateView, CustomerUpdateView, ProductCreateView, \
    ProductUpdateView, AdminComplaintUpdateView
from .views.auth_views import CustomLoginView, CustomLogoutView
from .views.employee_views import EmployeeDashboardView, AssignedComplaintsView, \
    UnassignedComplaintsView, ComplaintUpdateView, AssignToMeView

urlpatterns = [
    # Auth
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Admin Panel
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),

    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),

    # Customer
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(),
         name='customer_edit'),

    # Product
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),

    path('complaints/', ComplaintListView.as_view(), name='complaint_list'),
    path('complaints/add/', ComplaintCreateView.as_view(), name='complaint_create'),
    path('complaints/<int:pk>/edit/', AdminComplaintUpdateView.as_view(),
         name='complaint_edit'),

    # Employee Panel
    path('employee-dashboard/', EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('assigned-complaints/', AssignedComplaintsView.as_view(), name='assigned_complaints'),
    path('unassigned-complaints/', UnassignedComplaintsView.as_view(), name='unassigned_complaints'),
    path('complaints/<int:pk>/update/', ComplaintUpdateView.as_view(), name='update_complaint_status'),
    path('complaints/<int:pk>/assign/', AssignToMeView.as_view(), name='assign_to_me'),

]
