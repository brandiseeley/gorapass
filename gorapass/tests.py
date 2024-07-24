import json

from django.test import Client, TestCase

from gorapass.models import Hikes, Stamps

TEST_STAMP = {
    "id": 150,
    "stage_number": 18,
    "spp_number": "17",
    "stamp_name": "Kocbekov dom na Korošici",
    "elevation": 1808,
    "elevation_unit": "m",
    "alpine_club": "Celje-Matica",
    "region": "Kamnik",
    "route_type": "Main",
    "lat": 46.35612316,
    "lon": 14.63936863,
    "completed_at_date": "1970-01-01"
  }

TEST_HIKES = [
    {
        "stamp": 150,
        "hike_name": "Planina Podvežak - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/planina_podvezak_kocbekov_dom_na_korosici/3/199/237",
        "starting_point": "Planina Podvežak",
        "starting_point_elevation": 1500,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3319,
        "lon_start": 14.6726,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 460,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "nan",
        "page_views": 128304,
        "directions_to_start": "Go to the boulder.",
        "hike_description": "Easy when the weather is good.",
        "completed_at_date": "1970-01-01"
    },
    {
        "stamp": 150,
        "hike_name": "Robanov kot - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/robanov_kot_kocbekov_dom_na_korosici/3/199/1831",
        "starting_point": "Robanov kot",
        "starting_point_elevation": 650,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3948,
        "lon_start": 14.703,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 1300,
        "total_elevation_gain_units": "m",
        "difficulty_level": "zahtevna označena pot",
        "recommended_equipment_summer": "čelada",
        "recommended_equipment_winter": "čelada, cepin, dereze",
        "page_views": 30907,
        "directions_to_start": "A right after the boulder.",
        "hike_description": "Challenging, but rewarding hike",
        "completed_at_date": "1970-01-01"
    },
    {
        "stamp": 150,
        "hike_name": "Za Loncem - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/za_loncem_kocbekov_dom_na_korosici/3/199/1264",
        "starting_point": "Za Loncem",
        "starting_point_elevation": 980,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3262,
        "lon_start": 14.6543,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 1000,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "cepin, dereze",
        "page_views": 24803,
        "directions_to_start": "A left after the boulder.",
        "hike_description": "A very pretty hike.",
        "completed_at_date": "1970-01-01"
    },
]

class HikesTestCase(TestCase):
    def setUp(self):
        Stamps.objects.create(**TEST_STAMP)
        for hike in TEST_HIKES:
            hike_data = hike | { 'stamp': Stamps.objects.get(pk=150) }
            Hikes.objects.create(**hike_data)
        HikesTestCase.client = Client()

    def test_hikes_endpoint(self):
        """GET requests to the hikes endpoint give us a 200 status"""
        response = HikesTestCase.client.get('/gorapass/hikes')
        self.assertEqual(response.status_code, 200)

    def test_hike_endpoint(self):
        """Fetching a single hike from 'hikes/<hike_id>' gives us JSON with corrent attributes"""
        # Fetch the hike
        response = HikesTestCase.client.get('/gorapass/hikes/1')
        self.assertEqual(response.status_code, 200)
        # Compare response data with data used to create the hike
        data = json.loads(response.content)
        data.pop('id')
        self.assertEqual(data, TEST_HIKES[0])
