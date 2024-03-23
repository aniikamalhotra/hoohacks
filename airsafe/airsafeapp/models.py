from django.db import models

class volume_at_time(models.Model):
    time = models.CharField(max_length=10,default=0)
    volume = models.CharField(max_length=10,default=0)


class volume_dataset(models.Model):
    vDataset = models.OneToOneField(volume_at_time, on_delete=models.CASCADE, related_name = 'DataEntry')




