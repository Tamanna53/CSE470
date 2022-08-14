from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = 'Tamannas Exclusive Admin Panel'  
admin.site.index_title = 'Admin' 
admin.site.site_title = 'TamannasExclusive_Admin'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('store/',include('store.urls')),
    path('cart/', include('carts.urls')),    
    path('accounts/', include('accounts.urls')),
    path("",views.home,name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
