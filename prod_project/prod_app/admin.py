from django.contrib import admin
from .models import Chemical, Batch, ReagentContainer


admin.site.register(Chemical)
admin.site.register(Batch)
admin.site.register(ReagentContainer)
