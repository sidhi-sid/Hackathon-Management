from django.db import models

# Create your models here.

class Leader(models.Model):
    teamname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    statusid = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=40)
    email = models.CharField(max_length=255)
    contact = models.IntegerField()
    college = models.CharField(max_length=300)
    yearofstudy = models.CharField(max_length=10)
    branch = models.CharField(max_length=40)
    github = models.URLField(max_length=250, default="")
    linkedin = models.URLField(max_length=250, default="")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.teamname + '-' + self.firstname + self.lastname
