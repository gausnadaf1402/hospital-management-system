from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile=models.IntegerField(null=True)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return f"doctor(patient)"
    

