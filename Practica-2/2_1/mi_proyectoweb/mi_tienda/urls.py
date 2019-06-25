from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home_view),
    url(r'^ClaseA', views.utilitarios_view),
    url(r'^Berlinas', views.berlinas_view),
    url(r'^index', views.home_view),
]
