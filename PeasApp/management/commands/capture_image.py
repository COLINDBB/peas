from django.core.management.base import BaseCommand, CommandError
from PeasApp.models import Image
from django.utils import timezone
import os
import cv2

class Command(BaseCommand):
    help = "Captures an image from the attached webcam."

    def handle(self, *args, **options):

        # Get image
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        # Generate filename
        path = "/home/colin/PycharmProjects/PeasProject/peas/PeasApp/static/PeasApp/images"
        filename = timezone.localtime().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        # Write to disk
        success = cv2.imwrite(os.path.join(path, filename), frame)

        if success:
            # Save to db
            image = Image()
            image.timestamp = timezone.localtime()
            image.filename = filename
            image.save()
            print("Image succesfully captured and saved to: {}".format(filename))
        else:
            print("Issue writing image to: {}".format(filename))
