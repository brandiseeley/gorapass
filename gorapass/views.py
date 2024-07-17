from django.http import HttpResponse
from django.conf import settings

from gorapass.models import Stamp

import csv
import os

def index(request):
    return HttpResponse('Hello, World. This is Naya and Brandi\'s super cool app.')

def populate_database(request):
    # Delete any existing objects in the database
    Stamp.objects.all().delete()

    # Parse CSV into objects
    hike_data_path = os.path.join(settings.BASE_DIR, 'gorapass/hike_data/spp_locations_to_hikes.csv')
    with open(hike_data_path, newline='') as csvfile:
        rows = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            rows.append(row)

        attributes = rows[0]
        hikes = []
        stamp_names = []

        for row in rows[1:]:
            hike = {}
            for i in range(len(attributes)):
                # if we're processing a stamp name
                if i == 1:
                    stamp_name = row[i]
                    if not (stamp_name in stamp_names):
                        stamp_names.append(stamp_name)

                    hike['stamp_id'] = stamp_names.index(stamp_name)
                else:
                    hike[attributes[i]] = row[i]

            hikes.append(hike)

    # TODO (@brandiseeley): Right now, we're just adding in the stamp names. We'll need to save stamp
    #       names as we process the data, and then collect the id provided by the database.
    #       After ensuring that a stamp has been saved, we can save the hike itself and
    #       lookup the associated stamp id to use as its foreign key. - BS
    for name in stamp_names:
        stamp = Stamp(name=name)
        stamp.save()

    # TODO (@brandiseeley): Save Hikes to DB. Need to first create model. - BS

    return HttpResponse('Database re-populated')