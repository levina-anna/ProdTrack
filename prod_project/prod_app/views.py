from django.shortcuts import render


def index(request):
    context = {
        'title': 'Main page'
    }
    return render(request, 'prod_app/index.html', context)
