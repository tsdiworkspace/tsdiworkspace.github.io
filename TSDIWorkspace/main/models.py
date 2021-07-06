from django.db import models
from django.conf import settings

# Create your models here.

class Testing(models.Model):
    t1 = models.CharField(max_length=64)
    t2 = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.t1}, {self.t2}"



class Lease(models.Model):
    lessee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    leaseFrom = models.DateField()
    leaseTo = models.DateField()
    seat = models.CharField(max_length=64)
    rent = models.IntegerField()

    def __str__(self):
        return f"{self.id}: Seat: {self.seat}, Rent: {self.rent}, Lease From: {self.leaseFrom}, Lease To: {self.leaseTo}"



class Bill(models.Model):
    lessee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    dueDate = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.id} - Lessee: {self.lessee}, Due Date: {self.dueDate}, Amount: {self.amount}"



class ServiceRequest(models.Model):
    lessee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.TextField()
    solved = models.BooleanField()

    def __str__(self):
        return f"{self.id} - Lessee: {self.lessee}, Date: {self.date}, Description: {self.description}, Solved: {self.solved}"



class MailAndPackage(models.Model):
    lessee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    pickedUp = models.BooleanField()

    def __str__(self):
        return f"{self.id} - Lessee: {self.lessee}, Date: {self.date}, Picked Up: {self.pickedUp}"



class Notification(models.Model):
    lessee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.id} - Lessee: {self.lessee}, Date: {self.date}"

