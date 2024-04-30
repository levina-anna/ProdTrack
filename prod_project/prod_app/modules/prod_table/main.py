from prod_app.models import ReagentContainer


def get_container_data():
    return ReagentContainer.objects.select_related('batch', 'chemical').all()
