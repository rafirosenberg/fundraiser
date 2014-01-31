from django.db import models

# Create your models here.


# class Donor(models.Model):
#     donorId = models.AutoField(primary_key=True)
#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=20)
#     phone = models.IntegerField(max_length=10)
#     email = models.EmailField()

#     def __unicode__(self):
#         return self.lastName + ', ' + self.firstName

class Pledge(models.Model):
    donationId = models.AutoField(primary_key=True)
    time = models.TimeField(auto_now=True)
    # donor = models.ForeignKey(Donor)
    donor = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=160, null=True, blank=True)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(null=True, blank=True)

    class Meta:
       ordering = ["-time"]

    def __unicode__(self):
        return self.donor