from django.contrib import admin
from .models import Project

# Previous antes maty
# admin.site.register(Project)

# Permite visualizar todos los atributos de la entidad "Project"
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','slug','description','user')


admin.site.register(Project,ProjectAdmin)