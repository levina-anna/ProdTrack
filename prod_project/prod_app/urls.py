from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('prod_table/', prod_table, name='prod_table'),
    path('get_container_data/<int:container_id>/', get_container_data, name='get_container_data'),
    path('update_container_data/<int:container_id>/', update_container_data, name='update_container_data'),
]
