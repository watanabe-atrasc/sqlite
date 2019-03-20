from django.db import models

class WorkData(models.Model):    
    #id = models.AutoField(primary_key=True)
    SyainId = models.CharField(max_length=7, blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    StartTime = models.DateTimeField(blank=True, null=True)
    EndTime = models.DateTimeField(blank=True, null=True)
    MorningOffFlg = models.BooleanField(blank=True, null=True)
    AfternoonOffFlg = models.BooleanField(blank=True, null=True)
    UpdStartTime = models.DateTimeField(blank=True, null=True)
    UpdEndTime = models.DateTimeField(blank=True, null=True)
    UpdMorningOffFlg = models.BooleanField(blank=True, null=True)
    UpdAfternoonOffFlg = models.BooleanField(blank=True, null=True)
    UpdFlg = models.BooleanField(blank=True, null=True)

class SyainData(models.Model):
    SyainId = models.CharField(max_length=7, primary_key=True)
    PassWord = models.CharField(max_length=8)