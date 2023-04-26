from django.contrib import admin
# Register your models here.
from biodata.models import Biodata

class biodataAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Biodata,biodataAdmin)