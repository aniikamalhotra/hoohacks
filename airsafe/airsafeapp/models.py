from django.db import models

class mri_time(models.Model):
    time = models.CharField(max_lenth=10,default=0)
    dobutamine = models.CharField(max_length=10,default=0)




