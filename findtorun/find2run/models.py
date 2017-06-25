from django.db import models
# from django.contrib.postgres.fields import JSONField


class User(models.Model):
    email = models.EmailField(max_length=100,
                              primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50,
                            blank=True)


class Location(models.Model):
    email = models.ForeignKey(User)
    lattitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
