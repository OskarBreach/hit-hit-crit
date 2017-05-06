from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from xwingdata.models import Pilot, Upgrade, ReferenceCard, Condition, Source
from xwingdata.models.named_model import url_name

def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def pilots(request):
    pilot_list = Pilot.objects.order_by('id')
    template = loader.get_template('pilot_grid.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilot_by_id(request, id):
    pilot_list = Pilot.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_pilots.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-name', kwargs={'name': clean_name}))

    pilot_list = Pilot.objects.filter(url_name=name).order_by('id')
    template = loader.get_template('pilot_grid.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_ship(request, ship):
    clean_name = url_name(ship)
    if ship != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-ships', kwargs={'ship': clean_name}))

    pilot_list = Pilot.objects.filter(ship__url_name=ship).order_by('id')
    template = loader.get_template('pilot_grid.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_faction(request, faction):
    clean_name = url_name(faction)
    if faction != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-faction', kwargs={'faction': clean_name}))

    pilot_list = Pilot.objects.filter(faction__url_name=faction).order_by('id')
    template = loader.get_template('pilot_grid.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_primary_faction(request, primary_faction):
    clean_name = url_name(primary_faction)
    if primary_faction != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-primary-faction', kwargs={'primary_faction': clean_name}))

    pilot_list = Pilot.objects.filter(faction__primary_faction__url_name=primary_faction).order_by('id')
    template = loader.get_template('pilot_grid.html')
    context = {
        'card_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades(request):
    upgrade_list = Upgrade.objects.order_by('id')
    template = loader.get_template('upgrade_grid.html')
    context = {
        'card_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrade_by_id(request, id):
    upgrade_list = Upgrade.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_upgrades.html')
    context = {
        'card_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('upgrades-by-name', kwargs={'name': clean_name}))

    upgrade_list = Upgrade.objects.filter(url_name=name).order_by('id')
    template = loader.get_template('upgrade_grid.html')
    context = {
        'card_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades_by_slot(request, slot):
    clean_name = url_name(slot)
    if slot != clean_name:
        return HttpResponseRedirect(reverse('upgrades-by-slot', kwargs={'slot': clean_name}))

    upgrade_list = Upgrade.objects.filter(slot__url_name=slot).order_by('id')
    template = loader.get_template('upgrade_grid.html')
    context = {
        'card_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def reference_cards(request):
    reference_card_list = ReferenceCard.objects.order_by('id')
    template = loader.get_template('reference_card_grid.html')
    context = {
        'card_list': reference_card_list,
    }
    return HttpResponse(template.render(context, request))

def reference_card_by_id(request, id):
    reference_card_list = ReferenceCard.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_reference_cards.html')
    context = {
        'card_list': reference_card_list,
    }
    return HttpResponse(template.render(context, request))

def conditions(request):
    condition_list = Condition.objects.order_by('id')
    template = loader.get_template('condition_grid.html')
    context = {
        'card_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def condition_by_id(request, id):
    condition_list = Condition.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_conditions.html')
    context = {
        'card_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def condition_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('condition-by-name', kwargs={'name': clean_name}))

    condition_list = Condition.objects.filter(url_name=name).order_by('id')
    template = loader.get_template('expanded_conditions.html')
    context = {
        'card_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def sources(request):
    source_list = Source.objects.order_by('id')
    template = loader.get_template('source_grid.html')
    context = {
        'card_list': source_list,
    }
    return HttpResponse(template.render(context, request))

def source_by_id(request, id):
    source_list = Source.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_sources.html')
    context = {
        'card_list': source_list,
    }
    return HttpResponse(template.render(context, request))
