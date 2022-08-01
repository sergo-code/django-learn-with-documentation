from django.db import models


class TestDB(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class RouteTest(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return self.name
