from django.db import models

class Stamp(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# TODO (@brandiseeley): Create 'Hike' model. Register on admin site and populate via 'populate_database' view.