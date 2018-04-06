# Create your views here.
import cjson

from django.conf import settings
from django.http import HttpResponse

from mds.api.responses import *
from mds.clients.models import Client
FPATH = "/media/clients/app-android.apk"
VERSION = "2"

def version(request, *args, **kwargs):
    authenticated = getattr(request, "authenticated", False)
    if not authenticated:
        result = []
        result.append("Invalid credentials")
        return unauthorized(result)

    version = -1
    flavor = request.GET.get('flavor',None)
    if flavor:
        objs = Client.objects.filter(flavor=flavor)
    else:
        objs = Client.objects.all()
    if objs.count() > 0:
        obj = objs.last()
        message = [{
            "version" : obj.version,
            "app": obj.app.url if obj.app else ""
        }]
    else:
        message = [{
            "version": -1,
            "app": ""
            }]
    return json_succeed(**message)


def invalid_file(request, fname='invalid.apk'):
    response = HttpResponse(
        content_type='application/vnd.android.package-archive')
    response['Content-Disposition'] = 'attachment; filename=%s' % fname
    response['Content-Length'] = 0
    response.status_code = 400
    return response
    
def download_latest(request):
    authenticated = getattr(request, "authenticated", False)
    if not authenticated:
        return json_unauthorized(["Invalid credentials",])
    obj = Client.objects.order_by('-version_code').first()
    if not obj:
        return invalid_file(request)
    data = obj.app
    fname = data.name.split('/')[-1]
    response = HttpResponse(data,
            content_type='application/vnd.android.package-archive')
    response['Content-Disposition'] = 'attachment; filename=%s' % fname
    response['Content-Length'] = data.size
    response.status_code = 200
    return response
    
def download_latest_x_sendfile(request, filename):
    obj = Client.objects.order_by('-version_code').first()
    if not obj:
        return invalid_file(request)
    data = obj.app
    fname = data.name.split('/')[-1]
    response = HttpResponse(content_type='application/vnd.android.package-archive')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(fname)
    response['X-Sendfile'] = data.name
    response['Content-Length'] = data.size
    return response
    
def submit_crash(request):
    authenticated = getattr(request, "authenticated", False)
    if not authenticated:
        return json_unauthorized(["Invalid credentials",])
    if request.method == 'POST':
        form = CrashReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return json_succeed({ "created": form.instance.created.strftime("%Y-%m-%d'T'%H:%M:%S") })
        else:
            return json_fail([], code=400, errors=form.errors)
    else:
        return json_fail([], code=400)
