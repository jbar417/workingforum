from django.db import models

# Create your models here.
class forum(models.Model):
    name = models.CharField(max_length=30)
    slack_time = models.CharField(max_length=40)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    alt_text = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True, on_delete=models.CASCADE)
    discuss = models.TextField(max_length=1000)
