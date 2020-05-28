from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Image
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .forms import Picker



@require_http_methods(["GET","POST"])
def show_images(request):

    filenames = list()
    template = loader.get_template("PeasApp/show_image.html")

    if request.method == "POST":
        picker = Picker(request.POST)
        if picker.is_valid():
            date_start = picker.cleaned_data["date_start"]
            date_end = picker.cleaned_data["date_end"]
            print(date_start)
        else:
            return HttpResponse(template.render({"form":picker},request))
    else:
        date_start = timezone.now() - timezone.timedelta(minutes=30)
        date_end = timezone.now()
        picker = Picker(initial={
            "date_start": date_start,
            "date_end": date_end
        })

    relevent_files = Image.objects.filter(timestamp__gt=date_start).filter(timestamp__lte=date_end)

    for image in relevent_files:
        tmp = dict()
        local_time = image.timestamp.astimezone(tz=timezone.get_current_timezone())
        tmp["nickname"] = local_time.strftime("%Y %b %d %H:%M")
        tmp["filename"] = image.filename
        filenames.append(tmp)

    context = {
        "filenames" : filenames,
        "form": picker
    }

    template = loader.get_template("PeasApp/show_image.html")
    return HttpResponse(template.render(context, request))
