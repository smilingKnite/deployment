from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^new$', views.new),
url(r'^confirm/(?P<id>\d+)', views.confirmDelete),
url(r'^delete/(?P<id>\d+)', views.delete),
url(r'^course/(?P<id>\d+)', views.course),
url(r'^addcomment$', views.addcomment)

]