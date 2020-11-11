from django.contrib import admin

from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta :
        model = Cegorias


@admin.register(Cegorias)
class CategoriasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource


class AutorResource(resources.ModelResource):
    class Meta :
        model = Autor


@admin.register(Autor)
class CutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ["nombres", "apellidos", "correo"]
    list_display = ('nombres','estado','fecha_creacion','correo','apellidos',)
    resource_class = CategoriaResource


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass