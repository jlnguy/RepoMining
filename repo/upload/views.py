from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.urls import reverse
from pip.utils import logging
import csv
import io
import logging

def index(request):
    return render_to_response("upload/upload_page.html")

def error(request):
    response = render_to_response('404.html', {},
                                  context_instance = RequestContext(request))
    response.status_code = 404
    return response


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload/upload_page.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect(reverse("upload:upload_csv"))
        # if file is too large, return
        if csv_file.multiple_chunks():
            return HttpResponseRedirect(reverse("upload:upload_csv"))

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    csv_file = request.FILES["csv_file"]
    decoded_file = csv_file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)

    dates = []
    info = []

    for line in csv.reader(io_string, delimiter=','):

        time = line[0]
        data = line[1]

        if time == "." or data == ".":  # where there's a date with no data put ' . '
            continue

        elif time == " " or data == " ":  # testing for blanks
            continue

        else:  # only add them in here
            dates.append(time)
            info.append(data)

    return HttpResponseRedirect(reverse("upload:upload_csv"))



