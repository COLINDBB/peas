import os
import cv2
from django.core.management.base import BaseCommand
from django.utils import timezone
from PeasApp.models import Image
import PeasProject.settings as settings

class Command(BaseCommand):
    help = "Captures an image from the attached webcam."

    def handle(self, *args, **options):

        # Get image
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        # Generate filename
        filename = timezone.localtime().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        # Write to disk
        success = cv2.imwrite(os.path.join(settings.IMAGE_PATH, filename), frame)

        if success:
            # Save to db
            image = Image()
            image.timestamp = timezone.localtime()
            image.filename = filename
            image.save()
            print("Image succesfully captured and saved to: {}".format(filename))
        else:
            print("Issue writing image to: {}".format(filename))
