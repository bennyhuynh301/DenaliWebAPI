from django.http import HttpResponseBadRequest, HttpResponse
from .forms import UploadParentsLogFileForm
from django.views.decorators.csrf import csrf_exempt
from DenaliWebAPI.settings import BASE_DIR

import os


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadParentsLogFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            handle_uploaded_file(file_name, request.FILES['parent_log'])
            return HttpResponse('OK')
        else:
            return HttpResponseBadRequest()


def handle_uploaded_file(file_name, f):
    log_dir = os.path.join(BASE_DIR, 'ActivityLogs')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    file_path = os.path.join(log_dir, file_name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)