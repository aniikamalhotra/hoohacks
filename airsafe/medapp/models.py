from django.db import models

class diameter_at_time(models.Model):
    time = models.FloatField(max_length=10,default=0)
    diameter = models.FloatField(max_length=10, default=0)





