from django.db import models

# Create your models here.


CATEGORY_OPTIONS = (
    ('IT', 'IT'),
    ('Non IT', 'Non IT'),
    (''), ('')
)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
