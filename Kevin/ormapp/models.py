from django.db import models
from django.contrib import admin
class Movie(models.Model):
    mid=models.IntegerField()
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=100)
    mname=models.CharField(max_length=100)
    phone=models.IntegerField()
    datetime=models.DateTimeField()
    seats=models.IntegerField()
class MovieAdmin(admin.ModelAdmin):
    list_display=('mid','name','mail','mname','phone','datetime','seats')

