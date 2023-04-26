from django.contrib import admin
from service.models import Service,Servicecard
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')
admin.site.register(Service,ServiceAdmin)

class ServiceCards(admin.ModelAdmin):
    list_display = ('service_card_title','service_card_intro','service_image')
admin.site.register(Servicecard,ServiceCards)