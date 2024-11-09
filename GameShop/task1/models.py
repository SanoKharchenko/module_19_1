from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)  # username аккаунта
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)

    def __str__(self):
        return self.title