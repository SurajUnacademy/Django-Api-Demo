from django.db import models

# Create your models here.

#Creating company models.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    choices = models.CharField(max_length=50, choices=
                               (('IT', 'IT'),
                                ('Non IT', 'Non IT'),
                                ('Mobile Phones', 'Mobile Phones')
                                ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):  # overriding the parent class function.
        return self.name + ' ' + self.location
        


#Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    positions = models.CharField(max_length=50, choices=
                                 (('Manager','manager'),
                                  ('Software Engineer', 'SDE'),
                                  ('Product Manger','PM')
                                  ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
