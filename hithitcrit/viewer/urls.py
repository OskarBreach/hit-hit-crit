from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pilots/$', views.pilots),
    url(r'^pilots/(\d+)/$', views.pilot_by_id),
    url(r'^upgrades/$', views.upgrades),
    url(r'^upgrades/(\d+)/$', views.upgrade_by_id),
    url(r'^reference-cards/$', views.reference_cards),
    url(r'^reference-cards/(\d+)/$', views.reference_card_by_id),
    url(r'^conditions/$', views.conditions),
    url(r'^conditions/(\d+)/$', views.condition_by_id),
]
