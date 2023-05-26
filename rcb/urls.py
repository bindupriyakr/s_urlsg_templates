from django.urls import path
from rcb.views import *
app_name='ammu'
urlpatterns=[
    path('virat/', virat, name='virat')
]