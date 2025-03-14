from django.urls import path

from . import views

app_name = 'weathers'

urlpatterns = [
    path("", views.index, name="cities"),
    path("<int:pk>", views.detail, name="city"),
    path("weathers/", views.weathers, name="weathers"),
    path("add", views.add_city, name="city_add"),
    path("delete_city/<int:city_id>/", views.delete_city, name="delete_city"),
]