import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .models import Publication
from .forms import UploadFileForm


def smart_func(request):
    obj = get_object_or_404(Publication, pk=2)
    return render(request, 'smart.html', {'obj': obj})


def hardcoded_URL(request):
    return redirect('https://vk.com/im')


@require_safe
def index(request):
    context = {
        'title': 'Заголовок index',
    }
    return render(request, 'index.html', context=context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@require_http_methods(["GET", "POST"])
def relationship_m2m(request, year):
    if year == 1999:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        now = datetime.datetime.now()
        html = f"<html><body>It is now {now} {year}.</body></html>"
        return HttpResponse(html)
