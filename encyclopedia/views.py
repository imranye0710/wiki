from django.shortcuts import render

from . import util

from django.http import HttpResponse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if title in util.list_entries():
        return render(request, util.list_entries(title))
    else:
        return HttpResponse("Title does not exist.")

