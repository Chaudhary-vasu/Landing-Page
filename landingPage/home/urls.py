from django.urls import include, path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name = "home"),
    path('about-us/',views.aboutUs,name = "about"),
    path('services/',views.services,name = "services"),
    path('contact/',views.contact,name = "contact"),
    path('calculator/',views.calculation,name = "contact"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)