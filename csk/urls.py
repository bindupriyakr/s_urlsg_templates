from django.urls import path
from csk.views import *
app_name='develoveper'
urlpatterns=[
    path('msd/',msd,name='msd'),
]