from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class f_users(models.Model):
    user_Id = models.OneToOneField(User,on_delete=models.CASCADE)
    # user_Name = models.CharField(max_length=100, blank=False, null=False)
    user_Email = models.CharField(max_length=100, blank=False, null=False)
    # mobile_number = models.CharField(max_length=12, blank=False, null=False)

    class Meta:
        db_table = 'users'

class user_votes(models.Model):
    user_Id = models.CharField(max_length=100, blank=False, null=False)
    dish_Id = models.CharField(max_length=100, blank=False, null=False)
    dish_Name = models.CharField(max_length=100, blank=False, null=False)
    v_Date = models.DateField(auto_now_add=True)
    v_Time = models.TimeField(auto_now_add=True)


    class Meta:
        db_table = 'user_votes'