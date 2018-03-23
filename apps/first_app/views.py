from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        "course" : Course.objects.all(),
    }

    return render(request, "first_app/index.html", context)
def new(request):
    if request.method == "POST":

        errors = Course.objects.Validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        

    return redirect('/')

def confirmDelete(request, id):
    
        

    context = {
        "course" : Course.objects.get(id = id)

    }
    print course
    return render(request, "first_app/delete.html", context)


def delete(request, id):
    
    Course.objects.filter(id = id).delete()

    return redirect('/')

def course(request, id):
    

    context = {
        "course" : Course.objects.get(id = id),
        "comments": Comment.objects.all()

    }

    return render(request, 'first_app/course.html', context)

def addcomment(request):
    if request.method == "POST":
        id = request.POST['courseid']
        course = Course.objects.get(id = id)
        
        print request.POST['author']
        print request.POST['comment']
    comment = Comment.objects.create( comment= request.POST['comment'], author = request.POST['author'], course = course)
    print comment
    return redirect("/course/"+ id)