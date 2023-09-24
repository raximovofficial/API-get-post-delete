from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    # score = models.IntegerField()
    # month = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Studentlar ruyxati'
        verbose_name_plural = 'Studentlar Ruyxati'

    def __str__(self):
        return self.name
