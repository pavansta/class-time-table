from django.shortcuts import render

def welcome(req):
    return render(req, "website/welcome.html")



