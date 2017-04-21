from django.http import HttpResponse
from django.template import loader

from xwingdata.models import Pilot, Upgrade, ReferenceCard, Condition

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
