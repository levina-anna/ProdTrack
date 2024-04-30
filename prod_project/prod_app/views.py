import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import ReagentContainer, Chemical


def index(request):
    context = {
        'title': 'Main page'
    }
    return render(request, 'prod_app/index.html', context)


def prod_table(request):
    from .modules.prod_table import main as prod_table_module
    containers = prod_table_module.get_container_data()

    context = {
        'title': 'Prod table',
        'containers': containers,
    }
    return render(request, 'prod_app/prod_table.html', context)


def get_container_data(request, container_id):
    # print(f"container_id: {container_id}")
    try:
        container = ReagentContainer.objects.get(id=container_id)
        data = {
            'id': container.id,
            'batch__date_produced': container.batch.date_produced.strftime('%Y-%m-%d'),
            'container_number': container.container_number,
            'volume': container.volume,
            'chemical__name': container.chemical.name,
            'is_recyclable': container.is_recyclable,
            'purity_level': container.purity_level,
            'storage_condition': container.storage_condition,
            'notes': container.notes,
        }
        return JsonResponse(data)
    except ReagentContainer.DoesNotExist:
        return JsonResponse({'error': 'ReagentContainer not found'}, status=404)


@require_http_methods(["POST", "PUT"])
def update_container_data(request, container_id):
    try:
        data = json.loads(request.body)
        container = ReagentContainer.objects.get(id=container_id)

        container.container_number = data.get('container_number')
        container.volume = data.get('volume')
        container.is_recyclable = data.get('is_recyclable')
        container.purity_level = data.get('purity_level')
        container.storage_condition = data.get('storage_condition')
        container.notes = data.get('notes')

        if 'chemical_name' in data:
            container.chemical = Chemical.objects.get(name=data['chemical_name'])

        container.save()
        return JsonResponse({'status': 'success', 'message': 'Container updated successfully'})
    except ReagentContainer.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Container not found'}, status=404)
    except Chemical.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Chemical not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
