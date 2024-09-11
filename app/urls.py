from django.urls import path
from . import views

urlpatterns = [
    path("<str:location>/<str:distance>/", views.temp, name="temp")
]