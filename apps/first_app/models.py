from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def Validator(self, postData):

        errors = {}
        course = Course.objects.filter(name = postData['name'])

        print course
        if len(course) > 0:
            errors['exists'] = "Course already exists"
        if len(postData['name']) < 6:
            errors['name'] = "Course name must be at least 6 letters"
        if len(postData['description']) < 15:
            errors['description'] = "Description name must be at least 15 letters"
        
        return errors

class Course(models.Model):
    name = models.CharField(max_length=38)
    description = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    author = models.CharField(max_length=45)
    course = models.ForeignKey(Course, related_name = "comments")
    created_at = models.DateTimeField(auto_now = True)