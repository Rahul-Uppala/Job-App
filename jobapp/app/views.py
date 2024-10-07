from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost


job_title = [
"First Job",
"Second Job",
"Third job"
]

job_description = [
"First job description",
"Second job description",
"Third job description"
]

# Create your views here.
#def hello(request):
#    return HttpResponse("<h3>Hello World</h3>")

class Tempclass:
    x=5

def hello(request):
    # template = loader.get_template("app/hello.html")
    list = ["alpha", "beta"]
    temp = Tempclass
    is_authenticated = False
    context = {"name":"Django", "age":10 ,"first_list":list, "temp_object":temp, "is_authenticated":is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html",context)


def job_list(request):
   # <ul><li>Job 1</li> <li>Job 2</li> <li>Job 3</li></ul>
#    list_of_jobs = "<ul>"
#    for j in job_title:
#        job_id = job_title.index(j)  
#        detail_url = reverse('jobs_detail', args=(job_id,))
#        list_of_jobs += f"<li><a href= '{detail_url}'>{j}</li>"
#    list_of_jobs += "</ul>"
#    return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context={"jobs":jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home')) 
    #return HttpResponse(f"<h1>job details page {id}<h1>")
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        # context={"job_title":job_title[id],"job_description":job_description[id]}
        job = JobPost.objects.get(id=id)
        context={"job":job}
        return render(request,"app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
