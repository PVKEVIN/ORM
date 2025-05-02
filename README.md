# Ex02 Django ORM Web Application
##REG-NO:212224040159
## Date:22-04-2025 

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2025-04-17 110407](https://github.com/user-attachments/assets/0c0fa11c-e26b-4a9a-ad4c-30cc3aa9ce1e)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
FOR MODELS:
```
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


```
FOR ADMIN:
```
from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

```




## OUTPUT

![Screenshot 2025-04-22 212021](https://github.com/user-attachments/assets/cf63f93d-1404-4c26-a3f5-35d10d0af11d)

![Screenshot 2025-04-22 211653](https://github.com/user-attachments/assets/7d4736cd-fc8a-45ec-ad0a-0d0c65c1de0f)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

