from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)pilots/$', views.pilots, name='pilots'),
    url(r'^(?i)pilots/(\d+)/$', views.pilot_by_id, name='pilot-by-id'),
    url(r'^(?i)pilots/ship/(?P<ship>[-\w]+)/$', views.pilots_by_ship, name='pilots-by-ship'),
    url(r'^(?i)upgrades/$', views.upgrades, name='upgrades'),
    url(r'^(?i)upgrades/(\d+)/$', views.upgrade_by_id, name='upgrade-by-id'),
    url(r'^(?i)reference-cards/$', views.reference_cards, name='reference-cards'),
    url(r'^(?i)reference-cards/(\d+)/$', views.reference_card_by_id, name='reference-card-by-id'),
    url(r'^(?i)conditions/$', views.conditions, name='conditions'),
    url(r'^(?i)conditions/(\d+)/$', views.condition_by_id, name='condition-by-id'),
]
