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

def objects_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('objects-by-name', kwargs={'name': clean_name}))

    source_list = Source.objects.filter(name=name).order_by('id')
    pilot_list = Pilot.objects.filter(url_name=name).order_by('id')
    upgrade_list = Upgrade.objects.filter(url_name=name).order_by('id')
    condition_list = Condition.objects.filter(url_name=name).order_by('id')
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

def object_by_xws(request, xws):
    clean_name = url_name(xws)
    if xws != clean_name:
        return HttpResponseRedirect(reverse('objects-by-xws', kwargs={'name': clean_name}))

    pilot_list = Pilot.objects.filter(xws=xws).order_by('id')
    upgrade_list = Upgrade.objects.filter(xws=xws).order_by('id')
    condition_list = Condition.objects.filter(xws=xws).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'pilot_list': pilot_list,
        'upgrade_list': upgrade_list,
        'condition_list': condition_list,
    }
    return HttpResponse(template.render(context, request))

def pilots(request):
    pilot_list = Pilot.objects.order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilot_by_id(request, id):
    pilot_list = Pilot.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-name', kwargs={'name': clean_name}))

    pilot_list = Pilot.objects.filter(url_name=name).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_ship(request, ship):
    clean_name = url_name(ship)
    if ship != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-ships', kwargs={'ship': clean_name}))

    pilot_list = Pilot.objects.filter(ship__url_name=ship).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_faction(request, faction):
    clean_name = url_name(faction)
    if faction != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-faction', kwargs={'faction': clean_name}))

    pilot_list = Pilot.objects.filter(faction__url_name=faction).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'pilot_list': pilot_list,
    }
    return HttpResponse(template.render(context, request))

def pilots_by_primary_faction(request, primary_faction):
    clean_name = url_name(primary_faction)
    if primary_faction != clean_name:
        return HttpResponseRedirect(reverse('pilots-by-primary-faction', kwargs={'primary_faction': clean_name}))

    pilot_list = Pilot.objects.filter(faction__primary_faction__url_name=primary_faction).order_by('id')
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

def upgrade_by_id(request, id):
    upgrade_list = Upgrade.objects.filter(id=id).order_by('id')
    template = loader.get_template('expanded_details.html')
    context = {
        'upgrade_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades_by_name(request, name):
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('upgrades-by-name', kwargs={'name': clean_name}))

    upgrade_list = Upgrade.objects.filter(url_name=name).order_by('id')
    template = loader.get_template('grid.html')
    context = {
        'upgrade_list': upgrade_list,
    }
    return HttpResponse(template.render(context, request))

def upgrades_by_slot(request, slot):
    clean_name = url_name(slot)
    if slot != clean_name:
        return HttpResponseRedirect(reverse('upgrades-by-slot', kwargs={'slot': clean_name}))

    upgrade_list = Upgrade.objects.filter(slot__url_name=slot).order_by('id')
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
    clean_name = url_name(name)
    if name != clean_name:
        return HttpResponseRedirect(reverse('condition-by-name', kwargs={'name': clean_name}))

    condition_list = Condition.objects.filter(url_name=name).order_by('id')
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
