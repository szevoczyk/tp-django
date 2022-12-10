from django.urls import path
from . import views

urlpatterns=[
    path('home/<name>',views.home,name='home'),
    path('listing/', views.task_listing,name="listing"),
    path('listing_t/', views.task_listing_t,name="listing"),
    path('listing2/', views.task_listing2,name="listing"),
]