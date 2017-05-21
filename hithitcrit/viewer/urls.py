from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)name/(?P<slug>[\w-]+)/$', views.objects_by_name, name='objects-by-name'),
    url(r'^(?i)pilots/$', views.pilots, name='pilots'),
    url(r'^(?i)upgrades/$', views.upgrades, name='upgrades'),
    url(r'^(?i)pilots/(?P<slug>[\w-]+)/$', views.pilot_details, name='pilot-details'),
    url(r'^(?i)upgrades/(?P<slug>[\w-]+)/$', views.upgrade_details, name='upgrade-details'),
    url(r'^(?i)ship/(?P<slug>[\w-]+)/$', views.ship_details, name='ship-details'),
    url(r'^(?i)faction/(?P<slug>[\w-]+)/$', views.faction_details, name='faction-details'),
    url(r'^(?i)primary-faction/(?P<slug>[\w-]+)/$', views.primary_faction_details, name='primary-faction-details'),
    url(r'^(?i)slot/(?P<slug>[\w-]+)/$', views.slot_details, name='slot-details'),
    url(r'^(?i)reference-cards/(?P<slug>[\w-]+)/$', views.reference_card_details, name='reference-card-details'),
    url(r'^(?i)conditions/(?P<slug>[\w-]+)/$', views.condition_details, name='condition-details'),
    url(r'^(?i)sources/(?P<slug>[\w-]+)/$', views.source_details, name='source-details'),
]
