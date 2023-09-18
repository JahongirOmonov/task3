from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Oquv_markaz(models.Model):
    name = models.CharField(max_length=220, default='')
    xonalar_soni = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name


class oqituvchi(models.Model):
    ismi = models.CharField(max_length=215, default='')
    tel_nomer = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.ismi
