from django.shortcuts import render
from django.views import View

from plantations.domain.lib import get_all_plantations


class PlantationsListView(View):
    def get(self, request, *args, **kwargs):
        context = {"plantations": get_all_plantations()}
        return render(request, "index.html", context=context)


class CreatePlantationView(View):
    def post(self, request, *args, **kwargs):
        pass
