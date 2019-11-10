from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given detail"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Database models for users in the system"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrieve full name of User"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of User"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email




class Policy(models.Model):
    Policy_id=models.AutoField(primary_key=True)
    Date_Of_Purchase=models.CharField(max_length=255)
    Customer_id=models.IntegerField()
    Fuel=models.CharField(max_length=255)
    Vehicle_Segment=models.CharField(max_length=255)
    Premium=models.FloatField()
    bodily_injury_liability=models.BooleanField(default=False)
    personal_injury_protection=models.BooleanField(default=False)
    property_damage_liability=models.BooleanField(default=False)
    collision=models.BooleanField(default=False)
    comprehensive=models.BooleanField(default=False)
    Customer_Gender=models.CharField(max_length=255)
    Customer_Income_Group=models.CharField(max_length=255)
    Customer_Region=models.CharField(max_length=255)
    Customer_Marital_Status=models.BooleanField(default=False)
