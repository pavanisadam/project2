from django.shortcuts import render

# Create your views here.
def jinja_project(request):
    d={'name':'ANU','age':12}
    return render(request,'jinja_project.html',context=d)