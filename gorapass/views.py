import json
import os
import pandas as pd

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect

from gorapass.models import CompletedHikes
from gorapass.models import Stamps
from gorapass.models import Hikes
from gorapass.models import User

from .src.filter_models import ModelFilter

def index(request):
    return HttpResponse('Hello, World. This is Naya and Brandi\'s super cool app.')

def stamp(request, stamp_id):
    stamp_model = get_object_or_404(Stamps, pk=stamp_id)
    stamp_dict = model_to_dict(stamp_model)
    return JsonResponse(stamp_dict, safe=False)

def stamps(request):
    stamp_models = Stamps.objects.all()

    if request.method == 'GET':
        stamp_dict = [ model_to_dict(stamp) for stamp in stamp_models ]
    elif request.method == 'POST':
        # Filter out stamps if there is filtration criteria on the request
        # TODO: Check that the body is JSON before trying to use `loads`
        body = json.loads(request.body)
        if body and body['selectors']:
            selectors = json.loads(request.body)['selectors']
            valid_selectors_status = ModelFilter.validate_selectors(Stamps, selectors)
            if not valid_selectors_status['success']:
                return HttpResponseBadRequest(valid_selectors_status['message'])

            stamp_models = ModelFilter.filter_data(stamp_models, selectors)
        stamp_dict = [ model_to_dict(stamp) for stamp in stamp_models ]
    else:
        return HttpResponseBadRequest('Invalid method. Must use GET or POST.')

    return JsonResponse(stamp_dict, safe=False)

def hike(request, hike_id):
    hike_model = get_object_or_404(Hikes, pk=hike_id)
    hike_dict = model_to_dict(hike_model)
    return JsonResponse(hike_dict, safe=False)

def hikes(request):
    hike_models = Hikes.objects.all()

    if request.method == 'GET':
        hike_dicts = [ model_to_dict(stamp) for stamp in hike_models ]
    elif request.method == 'POST':
        # Filter out hikes if there is filtration criteria in the request
        # TODO: Check that the body is JSON before trying to use `loads`: json.decoder.JSONDecodeError
        body = json.loads(request.body)
        if body and body['selectors']:
            selectors = json.loads(request.body)['selectors']
            valid_selectors_status = ModelFilter.validate_selectors(Hikes, selectors)
            if not valid_selectors_status['success']:
                return HttpResponseBadRequest(valid_selectors_status['message'])

            hike_models = ModelFilter.filter_data(hike_models, selectors)

        hike_dicts = [ model_to_dict(hike) for hike in hike_models ]
    else:
        return HttpResponseBadRequest('Invalid method. Must use GET or POST.')

    return JsonResponse(hike_dicts, safe=False)

def user(request, user_id):
    if request.user.is_authenticated and request.user.pk == user_id:
        return JsonResponse(model_to_dict(request.user))
    else:
        return redirect('login')

def user_completed_hikes(request, user_id):
    if request.user.is_authenticated and request.user.pk == user_id:
        completed_hike_models = Hikes.objects.filter(completedhikes__user_id=user_id)
        hike_dicts = [ model_to_dict(hike) for hike in completed_hike_models ]
        return JsonResponse(hike_dicts, safe=False)
    else:
        return redirect('login')

def user_completed_stamps(request, user_id):
    if request.user.is_authenticated and request.user.pk == user_id:
        completed_stamp_models = Stamps.objects.filter(completedstamps__user_id=user_id)
        stamp_dicts = [ model_to_dict(stamp) for stamp in completed_stamp_models ]
        return JsonResponse(stamp_dicts, safe=False)
    else:
        return redirect('login')

def login_user(request):
    """A temporary view that should eventually respond to POST requests to log users in"""
    return HttpResponse('Login page goes here.')

def login_test_user(request):
    """A temporary view to log in a test user until we create the ability to log in different users"""
    user = authenticate(request, username='jane_doe', password='gorapass')
    if user is not None:
        login(request, user)
        return HttpResponse('Login successful')
    else:
        return HttpResponse('Login failed')

def logout_user(request):
    user = request.user
    logout(request)
    return HttpResponse(f'{user} has been logged out')

def populate_stamps_datatable(request):
    ## Reset data table to null
    Stamps.objects.all().delete()
    ## Get base data
    stamp_data_path = os.path.join(settings.BASE_DIR, 'gorapass/hike_data/stamp_data_for_app.csv')
    stamp_data_csv = pd.read_csv(stamp_data_path)
    ## Populate the data table
    for i in range(len(stamp_data_csv)):
        Stamps.objects.create(
            stage_number = stamp_data_csv['stage_number'][i],
            spp_number = stamp_data_csv['spp_number'][i],
            stamp_name = stamp_data_csv['stamp_name'][i],
            elevation = stamp_data_csv['elevation'][i],
            elevation_unit = stamp_data_csv['elevation_unit'][i],
            alpine_club = stamp_data_csv['alpine_club'][i],
            region = stamp_data_csv['region'][i],
            route_type = stamp_data_csv['route_type'][i],
            lat = stamp_data_csv['lat'][i],
            lon = stamp_data_csv['lon'][i],
            completed_at_date = '1970-01-01'
            )
    return HttpResponse('Data was reset')

def populate_hikes_datatable(request):
    ## Reset data table to null
    Hikes.objects.all().delete()
    ## Get base data
    hike_data_path = os.path.join(settings.BASE_DIR, 'gorapass/hike_data/matched_hikes_for_app.csv')
    hike_data_csv = pd.read_csv(hike_data_path)
    ## Populate the data table
    for i in range(len(hike_data_csv)):
        Hikes.objects.create(
            stamp = Stamps.objects.get(stamp_name=hike_data_csv['stamp_name'][i]),
            hike_name = hike_data_csv['hike_name'][i],
            hike_link = hike_data_csv['hike_link'][i],
            starting_point = hike_data_csv['starting_point'][i],
            starting_point_elevation = hike_data_csv['starting_point_elevation'][i],
            starting_point_elevation_units = hike_data_csv['starting_point_elevation_units'][i],
            lat_start = hike_data_csv['lat_start'][i],
            lon_start = hike_data_csv['lon_start'][i],
            ending_point = hike_data_csv['ending_point'][i],
            ending_point_elevation = hike_data_csv['ending_point_elevation'][i],
            ending_point_elevation_units = hike_data_csv['ending_point_elevation_units'][i],
            lat_end = hike_data_csv['lat_end'][i],
            lon_end = hike_data_csv['lon_end'][i],
            total_elevation_gain = hike_data_csv['total_elevation_gain'][i],
            total_elevation_gain_units = hike_data_csv['total_elevation_gain_units'][i],
            difficulty_level = hike_data_csv['difficulty_level'][i],
            recommended_equipment_summer = hike_data_csv['recommended_equipment_summer'][i],
            recommended_equipment_winter = hike_data_csv['recommended_equipment_winter'][i],
            page_views = hike_data_csv['page_views'][i],
            directions_to_start = hike_data_csv['directions_to_start'][i],
            hike_description = hike_data_csv['hike_description'][i],
            completed_at_date = '1970-01-01'
        )
    return HttpResponse('Data was reset')

def empty_hikes_datatable(request):
    ## Reset data table to null
    Hikes.objects.all().delete()
    return HttpResponse('Data was removed.')
