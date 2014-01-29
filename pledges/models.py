from django.db import models

# Create your models here.


class Donor(models.Model):
    donorId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()

    def __unicode__(self):  
        return self.lastName + ', ' + self.firstName

class Pledge(models.Model):
    donationId = models.AutoField(primary_key=True)
    time = models.DateField(auto_now=True)
    donor = models.ForeignKey(Donor)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __unicode__(self):  
        return self.donor.lastName + ', ' + self.donor.firstName