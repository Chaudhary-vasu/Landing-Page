from django.contrib import admin
from home.models import Home,HomeForm
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ('home_logo',)
    
admin.site.register(Home,HomeAdmin)

class formAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email')
    
admin.site.register(HomeForm,formAdmin)