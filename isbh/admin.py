from django.contrib import admin

# Register your models here.
from isbh.models import *
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Departamento)
admin.site.register(Localidad)
admin.site.register(Genero)
