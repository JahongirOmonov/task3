from django.urls import path
from .views import GetAllOquvMarkaz, PostOquvMarkaz, GetDetailOquvMarkaz, PatchOquvMarkaz, DeleteOquvMarkaz, AllFunctionOquvMarkaz, PostGetOquvMarkaz
from .views import GetAllOqituvchi, GetDetailOqituvchi, PostOqituvchi, PatchOqituvchi, DeleteOqituvchi, AllFunctionOqituvchi, PostGetOqituvchi



urlpatterns=[
    path('GetAllOquvMarkaz/', GetAllOquvMarkaz.as_view()),


    path('GetDetailOquvMarkaz/<int:pk>', GetDetailOquvMarkaz.as_view()),


    path('PostOquvMarkaz/', PostOquvMarkaz.as_view() ),

    path('PatchOquvMarkaz/<int:pk>', PatchOquvMarkaz.as_view()),
    path('DeleteOquvMarkaz/<int:pk>', DeleteOquvMarkaz.as_view()),
    path('PostGetOquvMarkaz/', PostGetOquvMarkaz.as_view()),


    path('AllFunctionOquvMarkaz/<int:pk>', AllFunctionOquvMarkaz.as_view()),
    path('GetAllOqituvchi/', GetAllOqituvchi.as_view()),
    path('GetDetailOqituvchi/<int:pk>', GetDetailOqituvchi.as_view()),
    path('PostOqituvchi/', PostOqituvchi.as_view() ),


    
    path('PatchOqituvchi/<int:pk>', PatchOqituvchi.as_view()),
    path('DeleteOqituvchi/<int:pk>', DeleteOqituvchi.as_view()),
    path('PostGetOqituvchi/', PostGetOqituvchi.as_view()),
    path('AllFunctionOqituvchi/<int:pk>', AllFunctionOqituvchi.as_view())


]