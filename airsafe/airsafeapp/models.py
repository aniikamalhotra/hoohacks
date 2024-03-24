from django.db import models

class volume_at_time(models.Model):
    time = models.IntegerField(max_length=10,default=0)
    volume = models.IntegerField(max_length=10,default=0)





