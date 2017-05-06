from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)name/(?P<name>[-\w\ ]+)/$', views.objects_by_name, name='objects-by-name'),
    url(r'^(?i)xws/(?P<xws>[-\w]+)/$', views.object_by_xws, name='object-by-xws'),
    url(r'^(?i)pilots/$', views.pilots, name='pilots'),
    url(r'^(?i)pilots/id/(?P<id>\d+)/$', views.pilot_by_id, name='pilot-by-id'),
    url(r'^(?i)pilots/name/(?P<name>[-\w\ ]+)/$', views.pilots_by_name, name='pilots-by-name'),
    url(r'^(?i)pilots/ship/(?P<ship>[-\w\ ]+)/$', views.pilots_by_ship, name='pilots-by-ship'),
    url(r'^(?i)pilots/faction/(?P<faction>[-\w\ ]+)/$', views.pilots_by_faction, name='pilots-by-faction'),
    url(r'^(?i)pilots/primary-faction/(?P<primary_faction>[\w\ ]+)/$', views.pilots_by_primary_faction, name='pilots-by-primary-faction'),
    url(r'^(?i)upgrades/$', views.upgrades, name='upgrades'),
    url(r'^(?i)upgrades/id/(?P<id>\d+)/$', views.upgrade_by_id, name='upgrade-by-id'),
    url(r'^(?i)upgrades/name/(?P<name>[-\w\ ]+)/$', views.upgrades_by_name, name='upgrades-by-name'),
    url(r'^(?i)upgrades/slot/(?P<slot>[-\w\ ]+)/$', views.upgrades_by_slot, name='upgrades-by-slot'),
    url(r'^(?i)reference-cards/$', views.reference_cards, name='reference-cards'),
    url(r'^(?i)reference-cards/id/(?P<id>\d+)/$', views.reference_card_by_id, name='reference-card-by-id'),
    url(r'^(?i)conditions/$', views.conditions, name='conditions'),
    url(r'^(?i)conditions/id/(?P<id>\d+)/$', views.condition_by_id, name='condition-by-id'),
    url(r'^(?i)conditions/name/(?P<name>[-\w\ ]+)/$', views.condition_by_name, name='condition-by-name'),
    url(r'^(?i)sources/$', views.sources, name='sources'),
    url(r'^(?i)sources/id/(?P<id>\d+)/$', views.source_by_id, name='source-by-id'),
]
