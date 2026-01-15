from django.db import models
from django.core.validators import RegexValidator


class Company(models.Model):

    COMPANY_TYPE_CHOICES = (
        ("startup", "Startup"),
        ("sme", "Small & Medium Enterprise"),
        ("enterprise", "Enterprise"),
        ("agency", "Agency"),
        ("other", "Other")
    )
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100, unique=True)
    location = models.CharField(max_length = 100)
    about = models.TextField(blank=True,)
    company_type = models.CharField(max_length = 30, choices = COMPANY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Employee(models.Model):
    POSITION_CHOICES = (
        ("intern", "Intern"),
        ("junior", "Junior Developer"),
        ("senior", "Senior Developer"),
        ("manager", "Manager"),
        ("hr", "HR"),
        ("admin", "Admin"),
        ("other", "Other")
    )
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.TextField(blank=True)
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\+?[0-9]{7,15}$",
                message="Enter a valid phone number",
            )
        ],
    )
    about = models.TextField(blank=True)
    employee_position = models.CharField(max_length = 30, choices = POSITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    class Meta:
        ordering = ["-created_at"]
