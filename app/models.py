from django.db import models

# Create your models here.
class Players(models.Model):
    sport=models.CharField(max_length=100,primary_key=True)
class WebPage(models.Model):
    sport=models.ForeignKey(Players('sport'),on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    url=models.URLField()
class AccessRecords(models.Model):
    name=models.ForeignKey(WebPage('name'),on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
