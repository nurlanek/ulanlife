from django.contrib import admin
from .models import Kroy_detail, Kroy, Masterdata, User
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from django.core.management import call_command
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import json
# Register your models here.

class MasterdataAdmin(admin.ModelAdmin):
    list_display = ("kroy_no","edinitsa", "created", "user")

class KroyAdmin(admin.ModelAdmin):
    list_display = ("kroy_no","name", "ras_tkani", "ras_dublerin", "edinitsa", "description", "created", "is_active",)
    search_fields = ("kroy_no",)
    list_editable = ("is_active",)

class Kroy_detailAdmin(admin.ModelAdmin):
    list_display = ("kroy", "pachka", "razmer", "rost", "stuk", "user" )
    search_fields = ("kroy",)

class UserAdmin(BaseUserAdmin):
    actions = ['export_selected', 'import_data']

    def export_selected(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=users_export.json'

        # Call the dumpdata command and write the output to the response
        call_command('dumpdata', 'auth.User', format='json', stdout=response)

        return response

    export_selected.short_description = "Export selected users as JSON"

    def import_data(self, request, queryset):
        # Assuming you have a JSON file named users_export.json
        file_path = 'path/to/users_export.json'

        with open(file_path, 'r') as file:
            data = json.load(file)

        # Use the loaddata command to import data
        call_command('loaddata', file_path)

    import_data.short_description = "Import data from JSON file"
class MyUserAdmin(ImportExportModelAdmin):
    pass

# Отменить предыдущую регистрацию модели UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Masterdata, MasterdataAdmin)
admin.site.register(Kroy, KroyAdmin)
admin.site.register(Kroy_detail, Kroy_detailAdmin)
