from django.db import models


class Crops(models.Model):
    """Модель культуры"""
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Duties(models.Model):
    """Модель пошлины на культуру"""
    crop = models.ForeignKey('Crops', on_delete=models.PROTECT, unique=True)
    duty = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'duties'

    def __str__(self):
        return self.crop.name
