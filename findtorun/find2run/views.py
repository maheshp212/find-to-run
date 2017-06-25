import json
import logging

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from utilities.utils import get_request_info

from find2run.models import User

logger = logging.getLogger(__name__)


@csrf_exempt
def signup(request):
    request_info = request.GET
    logger.debug("The data received is %s", json.dumps(request_info))
    User(email=request.GET['email']).save()
    return HttpResponse("User added")


def welcome(request):
    return HttpResponse('Welcome to find2run')


def login(request):
    request_info = request.GET
    logger.debug("The request received is %s", json.dumps(request_info))
    if User.objects.filter(email=request_info['email']).exists():
        return HttpResponse('exists')
    else:
        return HttpResponse('DoesNotExist')


@csrf_exempt
def update_location(request):
    request_info = request.GET
    try:
        a_user = User.objects.get(email=request_info['email'])
        a_user.lattitude = request_info['lattitude']
        a_user.longitude = request_info['longitude']
        a_user.save()
        return HttpResponse('Location updated')
    except Exception as e:
        logger.error(e, exc_info=True)
        return HttpResponse(e)


def get_locations(request):
    users = User.objects.all()
    locations = set()

    for a_user in users:
        if not a_user.lattitude:
            continue
        location = (a_user.lattitude,
                    a_user.longitude)
        locations.add(location)

    locations = list(locations)
    return HttpResponse(json.dumps(locations))


def get_users_in_location(request):
    request_info = request.GET
    users = User.objects.filter(lattitude=request_info['lattitude'],
                                longitude=request_info['longitude'])
    users_in_loc = []

    for a_user in users:
        user_dict = {}
        user_dict['email'] = a_user.email
        user_dict['first_name'] = a_user.first_name
        user_dict['last_name'] = a_user.last_name
        users_in_loc.append(user_dict)
    return HttpResponse(json.dumps(users_in_loc))
