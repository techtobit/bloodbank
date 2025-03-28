from ast import Not
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.contrib.auth import get_user_model
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, blood_group, division, district, upazila,  password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone Number is required')
        user=self.model(phone_number=phone_number, full_name=full_name, blood_group=blood_group, division=division, district=district, upazila=upazila,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, full_name, blood_group, division, district, upazila,  password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(phone_number, full_name, blood_group, division, district, upazila,  password, **extra_fields)

class UsersModel(AbstractBaseUser, PermissionsMixin):
    phone_number= models.CharField(max_length=11, unique=True, null=False)
    password= models.CharField(max_length=150, null=False)
    full_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    total_donation = models.IntegerField(default=0, blank=True)
    last_donation_date = models.DateField(null=True , blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects=CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password']
    
    def __str__(self):
        return f"{self.phone_number}"
    
class Feedback(models.Model):
    feedbacker_name=models.CharField(max_length=50)
    feedback_subject=models.CharField(max_length=50)
    feedback_details=models.CharField(max_length=350)
    created_at=models.DateField(auto_now_add=True)

class Report(models.Model):
    report_to_donar=models.BooleanField(default=False, blank=True)
    report_to_seeker=models.BooleanField(default=False, blank=True)
    own_phone_number=models.CharField(max_length=11, unique=True)
    reporting_phone_number=models.CharField(max_length=11)
    reporting_details=models.CharField(max_length=350)
    created_at=models.DateField(auto_now_add=True)