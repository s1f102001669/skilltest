from email.policy import default
from django.db import models

# Create your models here.
class Equestion(models.Model):
    number = models.IntegerField(default=0)
    ques = models.TextField()
    sele1 = models.TextField()
    sele2 = models.TextField()
    sele3 = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.ques

class Nquestion(models.Model):
    number = models.IntegerField(default=0)
    ques = models.TextField()
    answer = models.CharField(max_length=1)
    com = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ques

class Epercent(models.Model):
    ques = models.TextField()
    true = models.IntegerField(default = 0)
    false = models.IntegerField(default = 0)
    percent = models.IntegerField(default = 0)

    def __str__(self):
        return self.ques

class Npercent(models.Model):
    ques = models.TextField()
    true = models.IntegerField(default = 0)
    false = models.IntegerField(default = 0)
    percent = models.IntegerField(default = 0)

    def __str__(self):
        return self.ques
