from django.test import TestCase

from plantations.domain.lib import get_all_plantations
from plantations.models import Plantation


class GetAllPlantations(TestCase):
    def setUp(self) -> None:
        Plantation.objects.create(name="Plantation 1", description="Description 1")
        Plantation.objects.create(name="Plantation 2", description="Description 2")
        Plantation.objects.create(name="Plantation 3", description="Description 3")

    def test_get_all_plantations(self):
        result = get_all_plantations()
        self.assertEqual(len(result), 3)