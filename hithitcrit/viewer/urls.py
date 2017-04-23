from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)pilots/$', views.pilots, name='pilots'),
    url(r'^(?i)pilots/(?P<id>\d+)/$', views.pilot_by_id, name='pilot-by-id'),
    url(r'^(?i)pilots/ship/(?P<ship>[-\w]+)/$', views.pilots_by_ship, name='pilots-by-ship'),
    url(r'^(?i)pilots/faction/(?P<faction>[-\w]+)/$', views.pilots_by_faction, name='pilots-by-faction'),
    url(r'^(?i)pilots/primary-faction/(?P<primary_faction>[\w]+)/$', views.pilots_by_primary_faction, name='pilots-by-primary-faction'),
    url(r'^(?i)upgrades/$', views.upgrades, name='upgrades'),
    url(r'^(?i)upgrades/(?P<id>\d+)/$', views.upgrade_by_id, name='upgrade-by-id'),
    url(r'^(?i)reference-cards/$', views.reference_cards, name='reference-cards'),
    url(r'^(?i)reference-cards/(?P<id>\d+)/$', views.reference_card_by_id, name='reference-card-by-id'),
    url(r'^(?i)conditions/$', views.conditions, name='conditions'),
    url(r'^(?i)conditions/(?P<id>\d+)/$', views.condition_by_id, name='condition-by-id'),
]
