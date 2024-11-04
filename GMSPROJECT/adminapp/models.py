from datetime import datetime

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
    address=models.CharField(null=False, blank=False, default="")
    flag=models.IntegerField(null=False, blank=False, validators= [MinValueValidator(0), MaxValueValidator(1)], default=1)
    access=models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return str(self.uid)



class Grievance(models.Model):
    gid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    aid=models.IntegerField(null=False, blank=False)
    area=models.CharField(null=False, blank=False, default="")
    issue_choices=(("WATER", "WATER"), ("SEWAGE", "SEWAGE"), ("ELECTRICITY", "ELECTRICITY"),("STREETLIGHT", "STREETLIGHT"),("MUNICIPAL SERVICES", "MUNICIPAL SERVICES"), ("PARKS-PUBLIC SPACES", "PARKS-PUBLIC SPACES"), ("PUBLIC TRANSPORT", "PUBLIC TRANSPORT"), ("GOVT.SCHEMAS","GOVT.SCHEMAS"), ("OTHERS", "OTHERS"))
    issue_type=models.CharField(null=False, blank=False, choices=issue_choices)
    issue=models.CharField(blank=False, null=False)
    viewflag=models.IntegerField(blank=False, null=False, default=0)
    solvedflag=models.IntegerField(blank=False, null=False, default=0)
    postdt = models.DateTimeField(blank=False, null=False, default=datetime.now())
    viewdt = models.DateTimeField(blank=True, null=True)
    solvedt = models.DateTimeField(blank=True, null=True)
    solvedby=models.BigIntegerField(default=0)
    def __str__(self):
        return str(self.user.uid) if self.user else "No User"


class EditData(models.Model):
    eid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    edit_choices=(("MOBILE", "MOBILE"), ("NAME","NAME"), ("AREA", "AREA"), ("ADDRESS", "ADDRESS"))
    type=models.CharField(null=False, blank=False, choices=edit_choices)
    old=models.CharField(null=False, blank=False)
    new=models.CharField(null=False, blank=False)
    reason=models.CharField(null=False, blank=False)
    proof=models.FileField(upload_to = 'proofdata/')
    reqdt=models.DateTimeField(blank=False, null=False,default=datetime.now() )
    status=models.IntegerField(null=False, blank=False, default=0)
    def __str__(self):
        return str(self.user.uid)

class About(models.Model):
    sid = models.IntegerField(blank=False, null=False, default=1)
    data=models.CharField(null=True, blank=True)

class Contact(models.Model):
    sid = models.IntegerField(blank=False, null=False, default=1)
    data=models.CharField(null=True, blank=True)

class Usage(models.Model):
    sid = models.IntegerField(blank=False, null=False, default=1)
    data=models.CharField(null=True, blank=True)

class Notification(models.Model):
    id=models.AutoField(primary_key=True)
    sendby=models.ForeignKey(User, on_delete=models.CASCADE, related_name="sendby")
    touser=models.ForeignKey(User, on_delete=models.CASCADE, related_name="touser")
    notify=models.CharField(blank=False, null=False)
    status=models.IntegerField(blank=False, null=False, default=0)
    senddt=models.DateTimeField(blank=False, null=False, default=datetime.now())
    def __str__(self):
        return str(self.id)