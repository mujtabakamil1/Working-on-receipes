from django.db import models



# Create your models here.


class Student (models.Model):
    name = models.CharField(max_length=50)
    age=models.IntegerField(default=19)
    email =models.EmailField()


class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=70)


    def __str__(self) -> str:
        return self.car_name





