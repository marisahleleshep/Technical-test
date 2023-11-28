from django.urls import path

from .views import PlantationsListView

urlpatterns = [
    path("index", PlantationsListView.as_view(), name="plantations-list"),
]