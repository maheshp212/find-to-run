import json
import logging

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from utilities.utils import get_request_info

from find2run.models import User

logger = logging.getLogger(__name__)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        request_info = get_request_info(request)
        User(**request_info).save()
        return HttpResponse("User added")


def welcome(request):
    return HttpResponse('Welcome to find2run')


@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        request_info = get_request_info(request)
        try:
            a_user = User.objects.get(email=request_info['email'])
            a_user.lattitude = request_info['lattitude']
            a_user.longitude = request_info['longitude']
            a_user.save()
            return HttpResponse('Location updated')
        except Exception as e:
            logger.error(e, exc_info=True)
            return HttpResponse(e)
        
