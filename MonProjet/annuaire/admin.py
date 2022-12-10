from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ContactResource(resources.ModelResource):
   class Meta:
      model = Contact
class ContactAdmin(ImportExportModelAdmin):
   resource_class = ContactResource

admin.site.register(Contact,ContactAdmin)