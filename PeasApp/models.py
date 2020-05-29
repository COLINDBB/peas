from django.db import models

class Image(models.Model):
    timestamp = models.DateTimeField('Date and time of image capture', null=True)
    filename = models.CharField('Image filename', max_length=200)

class Timelapse(models.Model):
    filename = models.CharField('Timestamp filename', max_length=200)
    fps = models.IntegerField('video frames per second')
    num_frames = models.IntegerField('Number of frames in video')