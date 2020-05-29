from django.core.management.base import BaseCommand
from django.utils import timezone
from PeasApp.models import Image, Timelapse
import PeasProject.settings as settings
import cv2
import os


class Command(BaseCommand):
    def handle(self, *args, **options):

        # timelapse the the last hour of frames
        date_end = timezone.now()
        date_start = timezone.now() - timezone.timedelta(hours=1)
        files = Image.objects.filter(timestamp__gt=date_start, timestamp__lt=date_end)

        fourcc = cv2.VideoWriter_fourcc(*'VP90')
        fps = 20

        output_path = os.path.join(settings.TIMELAPSE_PATH, date_start.strftime("%Y-%m-%d_%H-%M-%S") + ".webm")

        videowriter = cv2.VideoWriter(
            output_path,
            fourcc,
            fps,
            (settings.IMAGE_WIDTH, settings.IMAGE_HEIGHT))

        num_frames = 0
        for file in files:
            pathToFile = os.path.join(settings.IMAGE_PATH, file.filename)
            mat = cv2.imread(pathToFile)
            videowriter.write(mat)
            num_frames += 1

        # Add entry to db
        record = Timelapse()
        record.fps = fps
        record.filename = date_start.strftime("%Y-%m-%d_%H-%M-%S") + ".webm"
        record.num_frames = num_frames
        record.save()