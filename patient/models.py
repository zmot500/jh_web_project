from django.db import models
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    idx=models.AutoField(primary_key=True)
    Pt_name=models.CharField(max_length=50, null=False)
    Pt_bdate=models.DateField(null=False)
    Pt_man=models.BooleanField(default=True, null=False)
    post_date=models.DateTimeField(default=datetime.now,\
                                   blank=True)
    
class Check(models.Model):
    sno=models.AutoField(primary_key=True)
    idx=models.ForeignKey("Patient", on_delete=models.CASCADE)
    in_date=models.DateField(null=False)
    in_db=models.IntegerField(null=False)
    in_wt=models.DecimalField(max_digits=5, decimal_places=2)
    in_bp_l=models.IntegerField(null=False)
    in_bp_h=models.IntegerField(null=False)
    post_date=models.DateTimeField(default=datetime.now,\
                                   blank=True)
    # Create your models here.
