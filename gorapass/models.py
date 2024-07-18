from django.db import models

class Stamps(models.Model):
    stage_number = models.IntegerField(unique=True)
    spp_number = models.TextField()
    stamp_name = models.TextField(unique=True)
    elevation = models.IntegerField()
    elevation_unit = models.TextField()
    alpine_club = models.TextField()
    region = models.TextField()
    route_type = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    completed_at_date = models.DateField()

    def __str__(self):
      return self.stamp_name

class Hikes(models.Model):
    stamp_name = models.TextField()   #.ForeignKey(Stamps, to_field='stamp_name', on_delete=models.CASCADE)
    hike_name = models.TextField()
    hike_link = models.URLField()
    starting_point = models.TextField()
    starting_point_elevation = models.IntegerField()
    starting_point_elevation_units = models.TextField()
    lat_start = models.FloatField()
    lon_start = models.FloatField()
    ending_point = models.TextField()
    ending_point_elevation = models.IntegerField()
    ending_point_elevation_units = models.TextField()
    lat_end = models.FloatField()
    lon_end = models.FloatField()
    total_elevation_gain = models.IntegerField()
    total_elevation_gain_units = models.TextField()
    difficulty_level = models.TextField()
    recommended_equipment_summer = models.TextField()
    recommended_equipment_winter = models.TextField()
    page_views = models.IntegerField()
    directions_to_start = models.TextField()
    hike_description = models.TextField()
    completed_at_date = models.DateField()

    def __str__(self):
      return self.hike_name