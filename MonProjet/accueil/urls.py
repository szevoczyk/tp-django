from django.contrib import admin
from django.urls import path, include, re_path
from .views import helloWorld, helloWorldWithTemplate,sum, sumTemplate

urlpatterns = [
    path('',helloWorld,name="hello-world"),
    path('template/',helloWorldWithTemplate, name="hello-world-with-template"),
    path('sum/<int:n1>/<int:n2>/',sum,name="sum"),
    re_path(r'^sum-regex/(?P<n1>[0-9]*)/(?P<n2>[0-9]*)',sum,name="sum-regex"),
    path('sum-template/<int:n1>/<int:n2>/',sumTemplate,name="sum-template"),
    # r'^products/(?P<pk>\d+)/$'

]