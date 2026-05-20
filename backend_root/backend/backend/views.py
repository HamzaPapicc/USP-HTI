from django.shortcuts import render

def frontend(request, path=None):
    return render(request, "index.html")
