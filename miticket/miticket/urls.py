from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'miticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('Aplicaciones.tickets.urls', namespace="tickets_app")),
    url(r'^admin/', include(admin.site.urls)),

    
]
