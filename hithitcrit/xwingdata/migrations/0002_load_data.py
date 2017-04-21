# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import decimal

from django.utils.dateparse import parse_date
from django.db import migrations
from shutil import copy
from hithitcrit.settings import XWING_DATA_DIR, MEDIA_ROOT

def load_definitions(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    PrimaryFaction = apps.get_model("xwingdata", "PrimaryFaction")
    PrimaryFaction.objects.using(db_alias).bulk_create([
        PrimaryFaction(primary_faction="Rebel"),
        PrimaryFaction(primary_faction="Imperial"),
        PrimaryFaction(primary_faction="Scum"),
        ])

    Faction = apps.get_model("xwingdata", "Faction")
    Faction.objects.using(db_alias).bulk_create([
        Faction(faction="Rebel Alliance", primary_faction=PrimaryFaction.objects.get(primary_faction="Rebel")),
        Faction(faction="Resistance", primary_faction=PrimaryFaction.objects.get(primary_faction="Rebel")),
        Faction(faction="First Order", primary_faction=PrimaryFaction.objects.get(primary_faction="Imperial")),
        Faction(faction="Galactic Empire", primary_faction=PrimaryFaction.objects.get(primary_faction="Imperial")),
        Faction(faction="Scum and Villainy", primary_faction=PrimaryFaction.objects.get(primary_faction="Scum")),
        ])
    #TODO: set up Faction images

    Size = apps.get_model("xwingdata", "Size")
    Size.objects.using(db_alias).bulk_create([
        Size(size="small"),
        Size(size="large"),
        Size(size="huge"),
        ])

    Action = apps.get_model("xwingdata", "Action")
    Action.objects.using(db_alias).bulk_create([
        Action(action="Barrel Roll"),
        Action(action="Boost"),
        Action(action="Cloak"),
        Action(action="Coordinate"),
        Action(action="Evade"),
        Action(action="Focus"),
        Action(action="Jam"),
        Action(action="Recover"),
        Action(action="Reinforce"),
        Action(action="Rotate Arc"),
        Action(action="SLAM"),
        Action(action="Target Lock"),
        ])

    Bearing = apps.get_model("xwingdata", "Bearing")
    Bearing.objects.using(db_alias).bulk_create([
        Bearing(id=0, name="Left Turn"),
        Bearing(id=1, name="Left Bank"),
        Bearing(id=2, name="Straight"),
        Bearing(id=3, name="Right Bank"),
        Bearing(id=4, name="Right Turn"),
        Bearing(id=5, name="Koiogran Turn"),
        Bearing(id=6, name="Segnor's Loop Left"),
        Bearing(id=7, name="Segnor's Loop Right"),
        Bearing(id=8, name="Tallon Roll Left"),
        Bearing(id=9, name="Tallon Roll Right"),
        Bearing(id=10, name="Backwards Left Bank"),
        Bearing(id=11, name="Backwards Straight"),
        Bearing(id=12, name="Backwards Right Bank"),
        ])

    Difficulty = apps.get_model("xwingdata", "Difficulty")
    Difficulty.objects.using(db_alias).bulk_create([
        Difficulty(id=1, name="White"),
        Difficulty(id=2, name="Green"),
        Difficulty(id=3, name="Red"),
        ])

    Slot = apps.get_model("xwingdata", "Slot")
    Slot.objects.using(db_alias).bulk_create([
        Slot(slot="Astromech"),
        Slot(slot="Bomb"),
        Slot(slot="Cannon"),
        Slot(slot="Cargo"),
        Slot(slot="Crew"),
        Slot(slot="Elite"),
        Slot(slot="Hardpoint"),
        Slot(slot="Illicit"),
        Slot(slot="Missile"),
        Slot(slot="Modification"),
        Slot(slot="Salvaged Astromech"),
        Slot(slot="System"),
        Slot(slot="Team"),
        Slot(slot="Tech"),
        Slot(slot="Title"),
        Slot(slot="Torpedo"),
        Slot(slot="Turret"),
        ])

def rollback_defintions(apps, schema_editor):
    # forwards_func() creates a number of instances,
    # so reverse_func() should delete them.
    db_alias = schema_editor.connection.alias

    Slot = apps.get_model("xwingdata", "Slot")
    Slot.objects.using(db_alias).filter(slot="Astromech").delete()
    Slot.objects.using(db_alias).filter(slot="Bomb").delete()
    Slot.objects.using(db_alias).filter(slot="Cannon").delete()
    Slot.objects.using(db_alias).filter(slot="Cargo").delete()
    Slot.objects.using(db_alias).filter(slot="Crew").delete()
    Slot.objects.using(db_alias).filter(slot="Elite").delete()
    Slot.objects.using(db_alias).filter(slot="Hardpoint").delete()
    Slot.objects.using(db_alias).filter(slot="Illicit").delete()
    Slot.objects.using(db_alias).filter(slot="Missile").delete()
    Slot.objects.using(db_alias).filter(slot="Modification").delete()
    Slot.objects.using(db_alias).filter(slot="Salvaged Astromech").delete()
    Slot.objects.using(db_alias).filter(slot="System").delete()
    Slot.objects.using(db_alias).filter(slot="Team").delete()
    Slot.objects.using(db_alias).filter(slot="Tech").delete()
    Slot.objects.using(db_alias).filter(slot="Title").delete()
    Slot.objects.using(db_alias).filter(slot="Torpedo").delete()
    Slot.objects.using(db_alias).filter(slot="Turret").delete()

    Difficulty = apps.get_model("xwingdata", "Difficulty")
    Difficulty.objects.using(db_alias).filter(name="White").delete()
    Difficulty.objects.using(db_alias).filter(name="Green").delete()
    Difficulty.objects.using(db_alias).filter(name="Red").delete()

    Bearing = apps.get_model("xwingdata", "Bearing")
    Bearing.objects.using(db_alias).filter(name="Left Turn").delete()
    Bearing.objects.using(db_alias).filter(name="Left Bank").delete()
    Bearing.objects.using(db_alias).filter(name="Straight").delete()
    Bearing.objects.using(db_alias).filter(name="Right Bank").delete()
    Bearing.objects.using(db_alias).filter(name="Right Turn").delete()
    Bearing.objects.using(db_alias).filter(name="Koiogran Turn").delete()
    Bearing.objects.using(db_alias).filter(name="Segnor's Loop Left").delete()
    Bearing.objects.using(db_alias).filter(name="Segnor's Loop Right").delete()
    Bearing.objects.using(db_alias).filter(name="Tallon Roll Left").delete()
    Bearing.objects.using(db_alias).filter(name="Tallon Roll Right").delete()
    Bearing.objects.using(db_alias).filter(name="Backwards Left Bank").delete()
    Bearing.objects.using(db_alias).filter(name="Backwards Straight").delete()
    Bearing.objects.using(db_alias).filter(name="Backwards Right Bank").delete()

    Action = apps.get_model("xwingdata", "Action")
    Action.objects.using(db_alias).filter(action="Barrel Roll").delete()
    Action.objects.using(db_alias).filter(action="Boost").delete()
    Action.objects.using(db_alias).filter(action="Cloak").delete()
    Action.objects.using(db_alias).filter(action="Coordinate").delete()
    Action.objects.using(db_alias).filter(action="Evade").delete()
    Action.objects.using(db_alias).filter(action="Focus").delete()
    Action.objects.using(db_alias).filter(action="Jam").delete()
    Action.objects.using(db_alias).filter(action="Recover").delete()
    Action.objects.using(db_alias).filter(action="Reinforce").delete()
    Action.objects.using(db_alias).filter(action="Rotate Arc").delete()
    Action.objects.using(db_alias).filter(action="SLAM").delete()
    Action.objects.using(db_alias).filter(action="Target Lock").delete()

    Size = apps.get_model("xwingdata", "Size")
    Size.objects.using(db_alias).filter(size="small").delete()
    Size.objects.using(db_alias).filter(size="large").delete()
    Size.objects.using(db_alias).filter(size="huge").delete()

    Faction = apps.get_model("xwingdata", "Faction")
    Faction.objects.using(db_alias).filter(faction="Rebel Alliance").delete()
    Faction.objects.using(db_alias).filter(faction="Resistance").delete()
    Faction.objects.using(db_alias).filter(faction="First Order").delete()
    Faction.objects.using(db_alias).filter(faction="Galactic Empire").delete()
    Faction.objects.using(db_alias).filter(faction="Scum and Villainy").delete()

    PrimaryFaction = apps.get_model("xwingdata", "PrimaryFaction")
    PrimaryFaction.objects.using(db_alias).filter(primary_faction="Rebel").delete()
    PrimaryFaction.objects.using(db_alias).filter(primary_faction="Imperial").delete()
    PrimaryFaction.objects.using(db_alias).filter(primary_faction="Scum").delete()

def load_ships(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Ship = apps.get_model('xwingdata', 'Ship')
    Dial = apps.get_model('xwingdata', 'Dial')
    Size = apps.get_model('xwingdata',  'Size')
    Action = apps.get_model('xwingdata',  'Action')
    Faction = apps.get_model('xwingdata',  'Faction')
    Bearing = apps.get_model('xwingdata',  'Bearing')
    Difficulty = apps.get_model('xwingdata',  'Difficulty')

    ships_data_file = os.path.join(XWING_DATA_DIR, 'data/ships.js')
    ships_data = json.loads(open(ships_data_file).read())

    for ship in ships_data:
        new_ship = Ship.objects.update_or_create(id=ship['id'],
                defaults={'name': ship['name'],
                    'attack': int(ship['attack']) if 'attack' in ship else None, 
                    'agility': int(ship['agility']),
                    'hull': int(ship['hull']),
                    'shields': int(ship['shields']),
                    'xws': ship['xws'],
                    'size': Size.objects.get(size=ship['size']),
                    'energy': int(ship['energy']) if 'energy' in ship else None,
                    'epic_points': decimal.Decimal(ship['epic_points']) if 'epic_points' in ship else None,})
        new_ship[0].faction.clear()
        for faction in ship['faction']:
            new_ship[0].faction.add(Faction.objects.get(faction=faction))
        new_ship[0].actions.clear()
        for action in ship['actions']:
            new_ship[0].actions.add(Action.objects.get(action=action))
        new_ship[0].maneuvers.clear()
        for speed in range(len(ship['maneuvers'])):
            for bearing in range(len(ship['maneuvers'][speed])):
                if ship['maneuvers'][speed][bearing] != 0:
                    difficulty = ship['maneuvers'][speed][bearing]
                    maneuvers_energy = ship['maneuvers_energy'][speed][bearing] if 'maneuvers_energy' in ship else None
                    Dial.objects.create(ship=new_ship[0], 
                            speed=speed, 
                            bearing=Bearing.objects.get(id=bearing), 
                            difficulty=Difficulty.objects.get(id=difficulty),
                            maneuvers_energy=maneuvers_energy) 

def rollback_ships(apps, schema_editor):
    pass

def load_conditions(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Condition = apps.get_model('xwingdata', 'Condition')

    conditions_data_file = os.path.join(XWING_DATA_DIR, 'data/conditions.js')
    conditions_data = json.loads(open(conditions_data_file).read())

    for condition in conditions_data:
        # Copy the condition images to MEDIA_ROOT directory
        if ('image' in condition):
            condition_image_from = os.path.join(XWING_DATA_DIR, 'images/', condition['image'])
            condition_image_to = os.path.join(MEDIA_ROOT, condition['image'])
            os.makedirs(os.path.dirname(condition_image_to), exist_ok=True)
            copy(condition_image_from, condition_image_to)

        Condition.objects.update_or_create(id=condition['id'], 
                defaults={'image': condition['image'] if 'image' in condition else "",
                    'name': condition['name'],
                    'xws': condition['xws'],
                    'text': condition['text'],
                    'unique': bool(condition['unique']),})

def rollback_conditions(apps, schema_editor):
    pass

def load_pilots(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Pilot = apps.get_model('xwingdata', 'Pilot')
    PilotSlot = apps.get_model('xwingdata', 'PilotSlot')
    Ship = apps.get_model('xwingdata', 'Ship')
    Condition = apps.get_model('xwingdata', 'Condition')
    Faction = apps.get_model('xwingdata',  'Faction')
    Slot = apps.get_model('xwingdata',  'Slot')

    pilots_data_file = os.path.join(XWING_DATA_DIR, 'data/pilots.js')
    pilots_data = json.loads(open(pilots_data_file).read())

    for pilot in pilots_data:
        # Copy the pilot images to MEDIA_ROOT directory
        if ('image' in pilot):
            pilot_image_from = os.path.join(XWING_DATA_DIR, 'images/', pilot['image'])
            pilot_image_to = os.path.join(MEDIA_ROOT, pilot['image'])
            os.makedirs(os.path.dirname(pilot_image_to), exist_ok=True)
            copy(pilot_image_from, pilot_image_to)

        new_pilot = Pilot.objects.update_or_create(id=pilot['id'],
                defaults={'name': pilot['name'],
                    'unique': bool(pilot['unique']) if 'unique' in pilot else False,
                    'ship': Ship.objects.get(name=pilot['ship']),
                    'skill': pilot['skill'] if pilot['skill'] != '?' else 0,
                    'skill_special_ruling': pilot['skill'] == '?',
                    'points': pilot['points'] if pilot['points'] != '?' else 0,
                    'points_special_ruling': pilot['points'] == '?',
                    'text': pilot['text'] if 'text' in pilot else "",
                    'image': pilot['image'] if 'image' in pilot else "",
                    'faction': Faction.objects.get(faction=pilot['faction']),
                    'xws': pilot['xws'],
                    'attack_override': pilot['ship_override']['attack'] if 'ship_override' in pilot else None,
                    'agility_override': pilot['ship_override']['agility'] if 'ship_override' in pilot else None,
                    'hull_override': pilot['ship_override']['hull'] if 'ship_override' in pilot else None,
                    'shields_override': pilot['ship_override']['shields'] if 'ship_override' in pilot else None,
                    'range': pilot['range'] if 'range' in pilot else "",})
        new_pilot[0].slots.clear()
        if 'slots' in pilot:
            for slot in pilot['slots']:
                PilotSlot.objects.update_or_create(pilot=new_pilot[0], slot=Slot.objects.get(slot=slot), defaults={
                    'quantity': PilotSlot.objects.filter(pilot=new_pilot[0], slot=Slot.objects.get(slot=slot)).count() + 1,})
        new_pilot[0].conditions.clear()
        if 'conditions' in pilot:
            for condition in pilot['conditions']:
                new_pilot[0].conditions.add(Condition.objects.get(name=condition))

def rollback_pilots(apps, schema_editor):
    pass

def load_upgrades(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Upgrade = apps.get_model('xwingdata', 'Upgrade')
    GrantsSlot = apps.get_model('xwingdata', 'GrantsSlot')
    Ship = apps.get_model('xwingdata', 'Ship')
    Condition = apps.get_model('xwingdata', 'Condition')
    Faction = apps.get_model('xwingdata', 'Faction')
    Slot = apps.get_model('xwingdata', 'Slot')
    Size = apps.get_model('xwingdata', 'Size')
    Action = apps.get_model('xwingdata', 'Action')

    upgrades_data_file = os.path.join(XWING_DATA_DIR, 'data/upgrades.js')
    upgrades_data = json.loads(open(upgrades_data_file).read())

    for upgrade in upgrades_data:
        # Copy the upgrade images to MEDIA_ROOT directory
        if ('image' in upgrade):
            upgrade_image_from = os.path.join(XWING_DATA_DIR, 'images/', upgrade['image'])
            upgrade_image_to = os.path.join(MEDIA_ROOT, upgrade['image'])
            os.makedirs(os.path.dirname(upgrade_image_to), exist_ok=True)
            copy(upgrade_image_from, upgrade_image_to)

        grants_stat = {}
        if 'grants' in upgrade:
            for grant in upgrade['grants']:
                if grant['type'] == "stats":
                    stat = grant['name']
                    value = grant['value']
                    if stat in grants_stat:
                        grants_stat[stat] += value
                    else:
                        grants_stat[stat] = value

        new_upgrade = Upgrade.objects.update_or_create(id=upgrade['id'],
                defaults={'name': upgrade['name'],
                    'slot': Slot.objects.get(slot=upgrade['slot']),
                    'slot_cost': 1,
                    'points': upgrade['points'],
                    'attack': upgrade['attack'] if 'attack' in upgrade else None,
                    'range': upgrade['range'] if 'range' in upgrade else "",
                    'text': upgrade['text'],
                    'image': upgrade['image'] if 'image' in upgrade else "",
                    'xws': upgrade['xws'],
                    'unique': bool(upgrade['unique']) if 'unique' in upgrade else False,
                    'effect': upgrade['effect'] if 'effect' in upgrade else "",
                    'faction': Faction.objects.get(faction=upgrade['faction']) if 'faction' in upgrade else None,
                    'limited': bool(upgrade['limited']) if 'limited' in upgrade else False,
                    'energy': upgrade['energy'] if 'energy' in upgrade else None,
                    'grants_attack': grants_stat['attack'] if 'attack' in grants_stat else None,
                    'grants_agility': grants_stat['agility'] if 'agility' in grants_stat else None,
                    'grants_hull': grants_stat['hull'] if 'hull' in grants_stat else None,
                    'grants_shields': grants_stat['shields'] if 'shield' in grants_stat else None,
                    'grants_skill': grants_stat['skill'] if 'skill' in grants_stat else None,})
        new_upgrade[0].grants_slot.clear()
        new_upgrade[0].grants_action.clear()
        if 'grants' in upgrade:
            for grant in upgrade['grants']:
                if grant['type'] == "slot":
                    slot = grant['name']
                    GrantsSlot.objects.update_or_create(upgrade=new_upgrade[0], slot=Slot.objects.get(slot=slot), defaults={
                        'quantity': GrantsSlot.objects.filter(upgrade=new_upgrade[0], slot=Slot.objects.get(slot=slot)).count() + 1,})
                elif grant['type'] == "action":
                    action = grant['name']
                    new_upgrade[0].grants_action.add(Action.objects.get(action=action))
        new_upgrade[0].ship.clear()
        if 'ship' in upgrade:
            for ship in upgrade['ship']:
                new_upgrade[0].ship.add(Ship.objects.get(name=ship))
        new_upgrade[0].size.clear()
        if 'size' in upgrade:
            for size in upgrade['size']:
                new_upgrade[0].size.add(Size.objects.get(size=size))
        new_upgrade[0].conditions.clear()
        if 'conditions' in upgrade:
            for condition in upgrade['conditions']:
                new_upgrade[0].conditions.add(Condition.objects.get(name=condition))

        #TODO: push this upstream
        Upgrade.objects.filter(xws__in=['emperorpalpatine', 'unguidedrockets', 'wookieecommandos', 'jabbathehutt', ]).update(slot_cost=2) 

def rollback_upgrades(apps, schema_editor):
    pass

def load_reference_cards(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    ReferenceCard = apps.get_model('xwingdata', 'ReferenceCard')

    reference_cards_data_file = os.path.join(XWING_DATA_DIR, 'data/reference-cards.js')
    reference_cards_data = json.loads(open(reference_cards_data_file).read())

    for reference_card in reference_cards_data:
        # Copy the pilot images to MEDIA_ROOT directory
        if ('image' in reference_card):
            reference_card_image_from = os.path.join(XWING_DATA_DIR, 'images/', reference_card['image'])
            reference_card_image_to = os.path.join(MEDIA_ROOT, reference_card['image'])
            os.makedirs(os.path.dirname(reference_card_image_to), exist_ok=True)
            copy(reference_card_image_from, reference_card_image_to)

        ReferenceCard.objects.update_or_create(id=reference_card['id'],
                defaults={'title': reference_card['title'],
                    'subtitle': reference_card['subtitle'],
                    'image': reference_card['image'] if 'image' in reference_card else "",
                    'text': reference_card['text'] if 'text' in reference_card else "",})

def rollback_reference_cards(apps, schema_editor):
    pass

def load_sources(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Source = apps.get_model('xwingdata', 'Source')
    Ship = apps.get_model('xwingdata', 'Ship')
    Pilot = apps.get_model('xwingdata', 'Pilot')
    Upgrade = apps.get_model('xwingdata', 'Upgrade')
    ReferenceCard = apps.get_model('xwingdata', 'ReferenceCard')
    Condition = apps.get_model('xwingdata', 'Condition')
    SourceShip = apps.get_model('xwingdata', 'SourceShip')
    SourcePilot = apps.get_model('xwingdata', 'SourcePilot')
    SourceUpgrade = apps.get_model('xwingdata', 'SourceUpgrade')

    sources_data_file = os.path.join(XWING_DATA_DIR, 'data/sources.js')
    sources_data = json.loads(open(sources_data_file).read())

    for source in sources_data:
        #Copy the source images to MEDIA_ROOT directory
        if ('image' in source):
            image_src = os.path.join(XWING_DATA_DIR, 'images/', source['image'])
            image_dest = os.path.join(MEDIA_ROOT, source['image'])
            os.makedirs(os.path.dirname(image_dest), exist_ok=True)
            copy(image_src, image_dest)

        if ('thumb' in source):
            thumb_src = os.path.join(XWING_DATA_DIR, 'images/', source['thumb'])
            thumb_dest = os.path.join(MEDIA_ROOT, source['thumb'])
            os.makedirs(os.path.dirname(thumb_dest), exist_ok=True)
            copy(thumb_src, thumb_dest)

        new_source = Source.objects.update_or_create(id=source['id'],
            defaults={  'name': source['name'],
                        'image': source['image'] if 'image' in source else "",
                        'thumb': source['thumb'] if 'thumb' in source else "",
                        'wave': source['wave'] if str(source['wave']).isnumeric() else None,
                        'special_wave_name': source['wave'] if not(str(source['wave']).isnumeric()) else "",
                        'released': bool(source['released']) if 'released' in source else False,
                        'sku': source['sku'],
                        'announcement_date': parse_date(source['announcement_date']),
                        'release_date': parse_date(source['release_date']) if 'release_date' in source else None, })
        contents = source['contents']
        new_source[0].ships.clear()
        if 'ships' in contents:
            for ship in contents['ships']:
                SourceShip.objects.create(source=new_source[0], ship=Ship.objects.get(id=ship), quantity=contents['ships'][ship])
        new_source[0].pilots.clear()
        if 'pilots' in contents:
            for pilot in contents['pilots']:
                SourcePilot.objects.create(source=new_source[0], pilot=Pilot.objects.get(id=pilot), quantity=contents['pilots'][pilot])
        new_source[0].upgrades.clear()
        if 'upgrades' in contents:
            for upgrade in contents['upgrades']:
                SourceUpgrade.objects.create(source=new_source[0], upgrade=Upgrade.objects.get(id=upgrade), quantity=contents['upgrades'][upgrade])
        new_source[0].reference_cards.clear()
        if 'reference-cards' in contents:
            for reference_card in contents['reference-cards']:
                new_source[0].reference_cards.add(ReferenceCard.objects.get(id=reference_card))
        new_source[0].conditions.clear()
        if 'conditions' in contents:
            for condition in contents['conditions']:
                new_source[0].conditions.add(Condition.objects.get(id=condition))

def rollback_sources(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('xwingdata', '0001_initial'),
    ]

    #TODO: Replace this migration with manage.py command
    operations = [
        migrations.RunPython(load_definitions, rollback_defintions),
        migrations.RunPython(load_ships, rollback_ships),
        migrations.RunPython(load_conditions, rollback_conditions),
        migrations.RunPython(load_pilots, rollback_pilots),
        migrations.RunPython(load_upgrades, rollback_upgrades),
        migrations.RunPython(load_reference_cards, rollback_reference_cards),
        migrations.RunPython(load_sources, rollback_sources),
    ]
