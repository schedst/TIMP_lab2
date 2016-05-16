from django.conf.urls import patterns, include,url
from django.contrib import admin
admin.autodiscover() #

urlpatterns = [
    url(r'^app/$', 'app.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
