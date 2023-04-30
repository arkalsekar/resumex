from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return render(request, 'index.html', {"name":"ranjeet"})

def resumeScanner(request):

    email = request.POST["email"]
    jd = request.POST["jd"]
    resume = request.POST["resume"]

    # print(email)
    # print(jd)
    # print(resume)

    result = "54%"
    
    return render(request, 'index.html', {"result":result})
