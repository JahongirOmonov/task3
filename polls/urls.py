from django.urls import path
from .views import getOquvMarkaz, postoquvmarkaz, detail

urlpatterns=[
    path('all/', getOquvMarkaz.as_view()),

    path('detail/<int:whichid>', detail),
    path('create/>', postoquvmarkaz.as_view())
]