from django.contrib import admin
from .models import ThingFolder, Thing, UoM


admin.site.register(ThingFolder)
admin.site.register(Thing)
admin.site.register(UoM)
