import json
from django.http import HttpResponseBadRequest

def get_json_data_or_401(request):
    """
    Used to parse and return JSON from a request that's expected
    to be a POST request containing JSON as the body
    """
    if request.method != 'POST':
        return HttpResponseBadRequest('Expected a POST request')
    if not request.body:
        return HttpResponseBadRequest('POST request must contain a body')

    try:
        data = json.loads(request.body)
    except ValueError:
        return HttpResponseBadRequest('Body must contain valid JSON')

    return data
