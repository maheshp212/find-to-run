import json


def get_request_info(request):
    request_info = {}
    request_info.update(json.loads(request.read().decode('utf-8')))
    return request_info
