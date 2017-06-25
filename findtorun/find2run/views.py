import json
import logging

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from find2run.models import User, Location

logger = logging.getLogger(__name__)


@csrf_exempt
def signup(request):
    request_info = request.GET
    logger.debug("The data received is %s", json.dumps(request_info))
    User(email=request.GET['email'],
         first_name=request.GET['first_name'],
         last_name=request.GET['last_name'],
         city=request.GET['city']).save()
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
        Location(email=User.objects.get(email=request.GET['email']),
                 lattitude=request_info['lattitude'],
                 longitude=request_info['longitude']).save()
        a_user.save()
        return HttpResponse('Location updated')
    except Exception as e:
        logger.error(e, exc_info=True)
        return HttpResponse(e)


def get_locations(request):
    location_obs = Location.objects.all()
    locations = set()

    for a_location in location_obs:
        location = (a_location.lattitude,
                    a_location.longitude)
        locations.add(location)

    locations = list(locations)
    return HttpResponse(json.dumps(locations))


def get_users_in_location(request):
    request_info = request.GET

    users_in_loc = []
    all_locations = Location.objects.filter(
        lattitude=request_info['lattitude'],
        longitude=request_info['longitude'])

    for a_location in all_locations:
        this_user = a_location.email.email
        if this_user not in users_in_loc:
            users_in_loc.append(this_user)
            # users_in_loc[this_user]['locations'] = []
            # all_user_locations = a_location.email.location_set.all()

            # for a_user_loc in all_user_locations:
            #     users_in_loc[this_user]['locations'].append(
            #         [a_user_loc.lattitude,
            #          a_user_loc.longitude])
        # this_loc = [a_location['lattitude'], a_location['longitude']]
        # all_locations.append(this_loc)
        
    # for a_user in users:
    #     user_dict = {}
    #     user_dict['email'] = a_user.email
    #     user_dict['first_name'] = a_user.first_name
    #     user_dict['last_name'] = a_user.last_name
    #     users_in_loc.append(user_dict)

    #     user_dict['locations'] = []

    #     all_locations = Location.objects.filter(email=a_user)
    #     for a_location in all_locations:
    #         this_loc = [a_location['lattitude'], a_location['longitude']]
    #         all_locations.append(this_loc)
    return HttpResponse(json.dumps(users_in_loc))
