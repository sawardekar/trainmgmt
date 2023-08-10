from django.db import models

# Create your models here.
STATUS = (
        ('Reserved', 'Reserved'),
        ('Open', 'Open'),
        ('Waiting', 'Waiting')
    )


class Train(models.Model):
    train_id = models.AutoField(primary_key=True, editable=False)
    train_name = models.CharField(max_length=120,blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)

    def _str_(self):
        return self.train_name


class Compartment(models.Model):
    comp_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=120,blank=True, null=True)

    def _str_(self):
        return self.name


class SeatAvabilty(models.Model):
    seat_id = models.AutoField(primary_key=True, editable=False)
    comp_id = models.ForeignKey(Compartment, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=10,blank=True, null=True)
    status = models.CharField(max_length=50,choices=STATUS,blank=True, null=True)
    user_name = models.CharField(max_length=200,blank=True, null=True)
    user_pancard = models.CharField(max_length=15,blank=True, null=True)
    user_mobile = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.user_name

