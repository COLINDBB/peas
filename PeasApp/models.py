from django.db import models

class Image(models.Model):
    timestamp = models.DateTimeField('Date and time of image capture', null = True)
    filename = models.CharField('Image filename', max_length = 50, null = True)
