# models.py

from django.db import models

class Brand(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Color(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/cars/')
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    yil = models.IntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.color}"
