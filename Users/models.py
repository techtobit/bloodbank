from ast import Not
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.contrib.auth import get_user_model
class CustomUserManager(BaseUserManager):
    def create_user(self, phoneNumber, full_name, blood_group, division, district, upazila,  password=None, **extra_fields):
        if not phoneNumber:
            raise ValueError('Phone Number is required')
        user=self.model(phoneNumber=phoneNumber, full_name=full_name, blood_group=blood_group, division=division, district=district, upazila=upazila, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phoneNumber, full_name, blood_group, division, district, upazila, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(phoneNumber, full_name, blood_group, division, district, upazila, password, **extra_fields)

class UsersModel(AbstractBaseUser, PermissionsMixin):
    phoneNumber= models.CharField(max_length=11, unique=True, null=False)
    password= models.CharField(max_length=150, null=False)
    full_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    
    objects=CustomUserManager()
    
    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = ['password']
    
    def __str__(self):
        return f"{self.phoneNumber}"

# class UserProfiles(models.Model):
#     user = models.OneToOneField(UsersModel, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=50)
#     blood_group = models.CharField(max_length=50)
#     division = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     upazila = models.CharField(max_length=100)