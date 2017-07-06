# Create your views here.
import cjson

from django.conf import settings
from django.http import HttpResponse

from mds.api.responses import JSONResponse, unauthorized
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
    return JSONResponse(cjson.encode({
        'status':'SUCCESS',
        'code':200, 
        'message': message}))
  