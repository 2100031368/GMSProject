from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Area(models.Model):
    id=models.AutoField(primary_key=True)
    area=models.CharField(null=False, blank=False,max_length=150)
    def __str__(self):
        return str(self.id) + self.area

class User(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.BigIntegerField(null=False, blank=False, unique=True, validators=[MinValueValidator(100000000000), MaxValueValidator(999999999999) ])
    name=models.CharField(null=False, blank=False,max_length=150)
    mobile=models.CharField(null=False, blank=False, max_length=13)
    aid=models.IntegerField(null=False, blank=False, default=0)
    flag=models.IntegerField(null=False, blank=False, validators= [MinValueValidator(0), MaxValueValidator(1)], default=1)
    access=models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return str(self.uid)



class Grievance(models.Model):
    gid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    aid=models.IntegerField(null=False, blank=False)
    name=models.CharField(null=False, blank=False)
    phno=models.CharField(null=False, blank=False, max_length=13)
    issue_choices=(("WATER", "WATER"), ("SEWAGE", "SEWAGE"), ("ELECTRICITY", "ELECTRICITY"),("STREETLIGHT", "STREETLIGHT"),("MUNICIPAL SERVICES", "MUNICIPAL SERVICES"), ("PARKS-PUBLIC SPACES", "PARKS-PUBLIC SPACES"), ("PUBLIC TRANSPORT", "PUBLIC TRANSPORT"), ("GOVT.SCHEMAS","GOVT.SCHEMAS"), ("OTHERS", "OTHERS"))
    issue_type=models.CharField(null=False, blank=False, choices=issue_choices)
    issue=models.CharField(blank=False, null=False)
    viewflag=models.IntegerField(blank=False, null=False, default=0)
    solvedflag=models.IntegerField(blank=False, null=False, default=0)
    def __str__(self):
        return str(self.uid)

