from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404

from xwingdata.models import Pilot, Upgrade, Ship, Faction, PrimaryFaction, Slot, ReferenceCard, Condition, Source

def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def objects_by_name(request, name):
    clean_name = slugify(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('objects-by-name', kwargs={'name': clean_name}))

    source_list = Source.objects.filter(name=name).order_by('id')
    pilot_list = Pilot.objects.filter(slug=name).order_by('id')
    upgrade_list = Upgrade.objects.filter(slug=name).order_by('id')
    condition_list = Condition.objects.filter(slug=name).order_by('id')
    reference_card_list = ReferenceCard.objects.filter(title=name).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'source_list': source_list,
        'pilot_list': pilot_list,
        'upgrade_list': upgrade_list,
        'condition_list': condition_list,
        'reference_card_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def pilots(request):
    pilot_list = Pilot.objects.order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilot_details(request, slug):
    pilot = get_object_or_404(Pilot, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'pilot_list': (pilot,),
    }
    return HttpResponse(template.render(context, request))

def ship_details(request, slug):
    ship = get_object_or_404(Ship, slug=slug)
    pilot_list = Pilot.objects.filter(ship=ship).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def faction_details(request, slug):
    faction = get_object_or_404(Faction, slug=slug)
    pilot_list = Pilot.objects.filter(faction=faction).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def primary_faction_details(request, slug):
    primary_faction = get_object_or_404(PrimaryFaction, slug=slug)
    pilot_list = Pilot.objects.filter(faction__primary_faction=primary_faction).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades(request):
    upgrade_list = Upgrade.objects.order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'upgrade_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrade_details(request, slug):
    upgrade = get_object_or_404(Upgrade, slug=slug)
    template = loader.get_template('expanded_details.html')
    context = {
        'upgrade_list': (upgrade,),
    }
    return HttpResponse(template.render(context, request))

def slot_details(request, slug):
    slot = get_object_or_404(Slot, slug=slug)
    upgrade_list = Upgrade.objects.filter(slot=slot).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'upgrade_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def reference_card_by_id(request, id):
    reference_card_list = ReferenceCard.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'reference_card_list': reference_card_list,
    }
    return HttpResponse(template.render(context, request))

def condition_by_id(request, id):
    condition_list = Condition.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'condition_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def condition_by_name(request, name):
    clean_name = slugify(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('condition-by-name', kwargs={'name': clean_name}))

    condition_list = Condition.objects.filter(slug=name).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'condition_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def source_by_id(request, id):
    source_list = Source.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'source_list': source_list,
    }
    return HttpResponse(template.render(context, request))
