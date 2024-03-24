from django.db import models

class volume_at_time(models.Model):
    time = models.FloatField(max_length=10,default=0)
    volume = models.FloatField(max_length=10,default=0)





