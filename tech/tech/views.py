from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request: HttpRequest):
    return render(request, "index.html")

@login_required
def members(request: HttpRequest):
    return render(request, "members.html")
