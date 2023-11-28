from plantations.models import Plantation


def get_all_plantations() -> list[Plantation]:
    return list(Plantation.objects.all())