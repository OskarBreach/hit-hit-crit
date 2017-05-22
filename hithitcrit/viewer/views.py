from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from xwingdata.models import Pilot, Upgrade, Ship, Faction, PrimaryFaction, Slot, Condition, Source

def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def objects_by_name(request, slug):
    pilot_list = Pilot.objects.filter(name_slug=slug).order_by('ship', 'faction__primary_faction', 'skill', 'points', 'name', 'faction')
    upgrade_list = Upgrade.objects.filter(name_slug=slug).order_by('slot', 'points', 'name')
    condition_list = Condition.objects.filter(name_slug=slug).order_by('points', 'name')

    if not (pilot_list or upgrade_list or condition_list):
        raise Http404

    template = loader.get_template('expanded_details.html')
    context = {
        'pilot_list': pilot_list,
        'upgrade_list': upgrade_list,
        'condition_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def pilot_grid(request):
    pilot_list = Pilot.objects.order_by('ship', 'faction__primary_faction', 'skill', 'points', 'name', 'faction')
    paginator = Paginator(pilot_list, 24)

    page = request.GET.get('page')
    try:
        pilots = paginator.page(page)
    except PageNotAnInteger:
        pilots = paginator.page(1)
    except EmptyPage:
        pilots = paginator.page(paginator.num_pages)

    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilots,
    }
    return HttpResponse(template.render(context, request))

def upgrade_grid(request):
    upgrade_list = Upgrade.objects.order_by('slot', 'points', 'name')
    paginator = Paginator(upgrade_list, 24)

    page = request.GET.get('page')
    try:
        upgrades = paginator.page(page)
    except PageNotAnInteger:
        upgrades = paginator.page(1)
    except EmptyPage:
        upgrades = paginator.page(paginator.num_pages)

    template = loader.get_template('grid.html')
    context = {
        'upgrade_list': upgrades,
    }
    return HttpResponse(template.render(context, request))

def pilot_details(request, slug):
    pilot = get_object_or_404(Pilot, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'pilot_list': (pilot,),
    }
    return HttpResponse(template.render(context, request))

def upgrade_details(request, slug):
    upgrade = get_object_or_404(Upgrade, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'upgrade_list': (upgrade,),
    }
    return HttpResponse(template.render(context, request))

def ship_details(request, slug):
    ship = get_object_or_404(Ship, slug=slug)
    pilot_list = Pilot.objects.filter(ship=ship).order_by('skill', 'points', 'name')
    template = loader.get_template('expanded_details.html')
    context = {
        'ship_list': (ship,),
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def faction_details(request, slug):
    faction = get_object_or_404(Faction, slug=slug)
    pilot_list = Pilot.objects.filter(faction=faction).order_by('ship', 'faction__primary_faction', 'skill', 'points', 'name', 'faction')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def primary_faction_details(request, slug):
    primary_faction = get_object_or_404(PrimaryFaction, slug=slug)
    pilot_list = Pilot.objects.filter(faction__primary_faction=primary_faction).order_by('ship', 'faction__primary_faction', 'skill', 'points', 'name', 'faction')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def slot_details(request, slug):
    slot = get_object_or_404(Slot, slug=slug)
    upgrade_list = Upgrade.objects.filter(slot=slot).order_by('slot', 'points', 'name')
    template = loader.get_template('grid.html')
    context = {
        'upgrade_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def condition_details(request, slug):
    condition = get_object_or_404(Condition, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'condition_list': (condition,),
    }
    return HttpResponse(template.render(context, request))

def source_details(request, slug):
    source = get_object_or_404(Source, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'source_list': (source,),
    }
    return HttpResponse(template.render(context, request))
