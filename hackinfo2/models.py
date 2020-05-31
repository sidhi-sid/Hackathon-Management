from django.db import models

# Create your models here.
class SignUpDetail(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    college = models.CharField(max_length=300)
    gender = models.CharField(max_length=255)
    phone = models.IntegerField()
    github = models.URLField(max_length=250, default="")
    linkedin = models.URLField(max_length=250, default="")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.username + '-' + self.email


class LeaderDetail(models.Model):
    teamname = models.CharField(max_length=255)
    statusid = models.AutoField(primary_key=True)
    firstname1 = models.CharField(max_length=255)
    lastname1 = models.CharField(max_length=255)
    gender1 = models.CharField(max_length=40)
    email1 = models.CharField(max_length=255)
    contact1 = models.IntegerField()
    college1 = models.CharField(max_length=300)
    yearofstudy1 = models.CharField(max_length=10)
    branch1 = models.CharField(max_length=40)
    github1 = models.URLField(max_length=250, default="")
    linkedin1 = models.URLField(max_length=250, default="")
    pub_date1 = models.DateTimeField()

    def __str__(self):
        return self.teamname 


class Organiser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Userdata(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
