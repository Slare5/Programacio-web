from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.index ),
    url( r'^test/(?P<id_ronda>[0-9])/$', views.encuesta ),
    url( r'^resultado/$', views.resultado ),
]