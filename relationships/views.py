from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
import datetime


def relationship_m2m(request, year):
    if year == 1999:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        now = datetime.datetime.now()
        html = f"<html><body>It is now {now} {year}.</body></html>"
        return HttpResponse(html)
