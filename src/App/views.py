from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import PageVisit

curr_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "Django Page"
    my_context = {
        "page_title" : my_title,
        "queryset" : queryset,
        "page_visit_count" : queryset.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)

def my_old_home_page_view(requests, *args, **kwargs):
    my_title = "Django Page"
    my_context = {
        "page-title" : my_title
    }
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hello Amigo</h1>
    </body>
    </html>""".format(**my_context)

    return HttpResponse(html_)