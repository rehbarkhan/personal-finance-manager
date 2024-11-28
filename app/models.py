from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.

class ModelBase(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']

class Profile(ModelBase):
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120)

    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=13)

    date_of_birth = models.DateField()

    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return 'Profile - {}'.format(self.email)

class Expense(ModelBase):
    _type = (
        ('credit','Credit'),
        ('debit','Debit'),
    )
    transaction_type = models.CharField(max_length=20, choices=_type)
    date = models.DateField()
    name = models.CharField(max_length=120)
    sum = models.FloatField()
    User = models.ForeignKey(User, related_name='ExpenseUser', on_delete=models.CASCADE, editable=False)


    def __str__(self):
        return '{} -> {}'.format(self.User.email, self.name)