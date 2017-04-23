from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pilots/$', views.pilots, name='pilots'),
    url(r'^pilots/(\d+)/$', views.pilot_by_id, name='pilot-by-id'),
    url(r'^(?i)pilots/ship/(?P<ship>[-\w]+)/$', views.pilots_by_ship, name='pilots-by-ship'),
    url(r'^upgrades/$', views.upgrades, name='upgrades'),
    url(r'^upgrades/(\d+)/$', views.upgrade_by_id, name='upgrade-by-id'),
    url(r'^reference-cards/$', views.reference_cards, name='reference-cards'),
    url(r'^reference-cards/(\d+)/$', views.reference_card_by_id, name='reference-card-by-id'),
    url(r'^conditions/$', views.conditions, name='conditions'),
    url(r'^conditions/(\d+)/$', views.condition_by_id, name='condition-by-id'),
]
