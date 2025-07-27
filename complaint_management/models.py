from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EMPLOYEE = "EMPLOYEE", "Employee"

    role = models.CharField(max_length=10, choices=Role.choices)

    def __str__(self):
        return self.username

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Customer(TimeStampedModel):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(unique=True)
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(TimeStampedModel):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Complaint(TimeStampedModel):
    class ComplaintLevel(models.TextChoices):
        LEVEL_1 = "LEVEL_1", "Level 1"
        LEVEL_2 = "LEVEL_2", "Level 2"
        LEVEL_3 = "LEVEL_3", "Level 3"

    class ComplaintStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        NOT_CLOSED = "NOT_CLOSED", "Not Closed"
        CLOSED = "CLOSED", "Closed"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                     related_name='complaints')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                    related_name='complaints')
    complaint_level = models.CharField(max_length=10,
                                           choices=ComplaintLevel.choices)
    description = models.TextField()
    location = models.CharField(max_length=255,
                                    help_text="Store latitude,longitude or address")
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL,
                                              null=True, blank=True,
                                              related_name='assigned_complaints')
    report = models.TextField(null=True, blank=True,
                                  help_text="Report or remarks on the complaint")
    status = models.CharField(max_length=20, choices=ComplaintStatus.choices,
                                  default=ComplaintStatus.PENDING,
                                  help_text="Current status of the complaint")

    def __str__(self):
        return f"Complaint #{self.id} - {self.customer.name}"





