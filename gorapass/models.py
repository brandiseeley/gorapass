from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User

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
    stamp = models.ForeignKey(Stamps, on_delete=models.CASCADE)
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

class CompletedStamps(models.Model):
    stamp = models.ForeignKey(Stamps, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['stamp', 'user'], name='unique_stamp_to_user'),
        ]

    def __str__(self):
        return f'User: {self.user} has completed stamp: {self.stamp}'

class CompletedHikes(models.Model):
    hike = models.ForeignKey(Hikes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['hike', 'user'], name='unique_hike_to_user'),
        ]

    def __str__(self):
        return f'User: {self.user} has completed hike: {self.hike}'
