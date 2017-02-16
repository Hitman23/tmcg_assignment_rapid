from django.views import generic
from django.shortcuts import render
from models import Groups, GetData
import SimpleHTTPServer
import SocketServer
from temba_client.v2 import TembaClient
from task import callData


# Create your views here.

def Index(request):
    group = Groups.objects.all()
    callData.delay()
    return render(request, 'api/index.html', {'groups': group})

