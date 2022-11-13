from tkinter import N
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser

phone_validator = RegexValidator(
    r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class Department(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    created_by = models.CharField(max_length=40)
    created_at = models.TimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=200, validators=[
                             phone_validator], unique=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    created_by = models.CharField(max_length=40)
    created_at = models.TimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["phone", "email"]


class Ticket_model(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=20)
    subject = models.CharField(max_length=40)
    body = models.TextField()
    priority = models.CharField(max_length=20, choices=[])
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    created_at = models.DateField(auto_now_add=True)


