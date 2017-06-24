import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from utilities.utils import get_request_info

from find2run.models import User


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        request_info = get_request_info(request)
        User(**request_info).save()
        return HttpResponse("User added")
