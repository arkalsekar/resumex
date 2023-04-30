from django.shortcuts import render
from django.http import HttpResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.


def hello(request):
    return render(request, 'index.html', {"name":"ranjeet"})

def resumeScanner(request):

    email = request.POST["email"]
    job_description = request.POST["jd"]
    resume = request.POST["resume"]

    # print(email)
    # print(jd)
    # print(resume)

    content_list = [job_description,resume]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(content_list)

    matrix = cosine_similarity(count_matrix)
    result = (matrix[1][0]*100).round(2)
    
    return render(request, 'index.html', {"result":result})
