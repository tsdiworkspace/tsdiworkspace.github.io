from django.db import models

# Create your models here.

class Testing(models.Model):
    t1 = models.CharField(max_length=64)
    t2 = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.t1}, {self.t2}"
