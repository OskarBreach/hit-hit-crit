# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import decimal

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.utils.dateparse import parse_date
from shutil import copy
from hithitcrit.settings import XWING_DATA_DIR, MEDIA_ROOT

import xwingdata.models as models

class Command(BaseCommand):
    help = 'Load data into the schema independently of migrations'
    
    def load_definitions(self):
        # We get the model from the versioned app registry;
        # if we directly import it, it'll be the wrong version
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        
        PrimaryFaction = models.PrimaryFaction
        PrimaryFaction(name="Rebel").save()
        PrimaryFaction(name="Imperial").save()
        PrimaryFaction(name="Scum").save()
        
        Faction = models.Faction
        Faction(name="Rebel Alliance", primary_faction=PrimaryFaction.objects.get(name="Rebel")).save()
        Faction(name="Resistance", primary_faction=PrimaryFaction.objects.get(name="Rebel")).save()
        Faction(name="First Order", primary_faction=PrimaryFaction.objects.get(name="Imperial")).save()
        Faction(name="Galactic Empire", primary_faction=PrimaryFaction.objects.get(name="Imperial")).save()
        Faction(name="Scum and Villainy", primary_faction=PrimaryFaction.objects.get(name="Scum")).save()
        #TODO: set up Faction images

        Size = models.Size
        Size.objects.using(db_alias).bulk_create([
            Size(size="small"),
            Size(size="large"),
            Size(size="huge"),
            ])

        Action = models.Action
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

        Bearing = models.Bearing
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

        Difficulty = models.Difficulty
        Difficulty.objects.using(db_alias).bulk_create([
            Difficulty(id=1, name="White"),
            Difficulty(id=2, name="Green"),
            Difficulty(id=3, name="Red"),
            ])

        Slot = models.Slot
        Slot(name="Astromech").save()
        Slot(name="Bomb").save()
        Slot(name="Cannon").save()
        Slot(name="Cargo").save()
        Slot(name="Crew").save()
        Slot(name="Elite").save()
        Slot(name="Hardpoint").save()
        Slot(name="Illicit").save()
        Slot(name="Missile").save()
        Slot(name="Modification").save()
        Slot(name="Salvaged Astromech").save()
        Slot(name="System").save()
        Slot(name="Team").save()
        Slot(name="Tech").save()
        Slot(name="Title").save()
        Slot(name="Torpedo").save()
        Slot(name="Turret").save()

    def rollback_definitions(self):
        # forwards_func() creates a number of instances,
        # so reverse_func() should delete them.
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias

        Slot = models.Slot
        Slot.objects.using(db_alias).filter(name="Astromech").delete()
        Slot.objects.using(db_alias).filter(name="Bomb").delete()
        Slot.objects.using(db_alias).filter(name="Cannon").delete()
        Slot.objects.using(db_alias).filter(name="Cargo").delete()
        Slot.objects.using(db_alias).filter(name="Crew").delete()
        Slot.objects.using(db_alias).filter(name="Elite").delete()
        Slot.objects.using(db_alias).filter(name="Hardpoint").delete()
        Slot.objects.using(db_alias).filter(name="Illicit").delete()
        Slot.objects.using(db_alias).filter(name="Missile").delete()
        Slot.objects.using(db_alias).filter(name="Modification").delete()
        Slot.objects.using(db_alias).filter(name="Salvaged Astromech").delete()
        Slot.objects.using(db_alias).filter(name="System").delete()
        Slot.objects.using(db_alias).filter(name="Team").delete()
        Slot.objects.using(db_alias).filter(name="Tech").delete()
        Slot.objects.using(db_alias).filter(name="Title").delete()
        Slot.objects.using(db_alias).filter(name="Torpedo").delete()
        Slot.objects.using(db_alias).filter(name="Turret").delete()

        Difficulty = models.Difficulty
        Difficulty.objects.using(db_alias).filter(name="White").delete()
        Difficulty.objects.using(db_alias).filter(name="Green").delete()
        Difficulty.objects.using(db_alias).filter(name="Red").delete()

        Bearing = models.Bearing
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

        Action = models.Action
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

        Size = models.Size
        Size.objects.using(db_alias).filter(size="small").delete()
        Size.objects.using(db_alias).filter(size="large").delete()
        Size.objects.using(db_alias).filter(size="huge").delete()

        Faction = models.Faction
        Faction.objects.using(db_alias).filter(name="Rebel Alliance").delete()
        Faction.objects.using(db_alias).filter(name="Resistance").delete()
        Faction.objects.using(db_alias).filter(name="First Order").delete()
        Faction.objects.using(db_alias).filter(name="Galactic Empire").delete()
        Faction.objects.using(db_alias).filter(name="Scum and Villainy").delete()

        PrimaryFaction = models.PrimaryFaction
        PrimaryFaction.objects.using(db_alias).filter(name="Rebel").delete()
        PrimaryFaction.objects.using(db_alias).filter(name="Imperial").delete()
        PrimaryFaction.objects.using(db_alias).filter(name="Scum").delete()

    def load_ships(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        Ship = models.Ship
        Dial = models.Dial 
        Size = models.Size
        Action = models.Action
        Faction = models.Faction
        Bearing = models.Bearing
        Difficulty = models.Difficulty

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
                new_ship[0].faction.add(Faction.objects.get(name=faction))
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

    def rollback_ships(self):
        pass 

    def load_conditions(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        Condition = models.Condition

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

    def rollback_conditions(self):
        pass

    def load_pilots(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        Pilot = models.Pilot
        PilotSlot = models.PilotSlot
        Ship = models.Ship
        Condition = models.Condition
        Faction = models.Faction
        Slot = models.Slot

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
                        'faction': Faction.objects.get(name=pilot['faction']),
                        'xws': pilot['xws'],
                        'attack_override': pilot['ship_override']['attack'] if 'ship_override' in pilot else None,
                        'agility_override': pilot['ship_override']['agility'] if 'ship_override' in pilot else None,
                        'hull_override': pilot['ship_override']['hull'] if 'ship_override' in pilot else None,
                        'shields_override': pilot['ship_override']['shields'] if 'ship_override' in pilot else None,
                        'range': pilot['range'] if 'range' in pilot else "",})
            new_pilot[0].slots.clear()
            if 'slots' in pilot:
                for slot in pilot['slots']:
                    PilotSlot.objects.update_or_create(pilot=new_pilot[0], slot=Slot.objects.get(name=slot), defaults={
                        'quantity': PilotSlot.objects.filter(pilot=new_pilot[0], slot=Slot.objects.get(name=slot)).count() + 1,})
            new_pilot[0].conditions.clear()
            if 'conditions' in pilot:
                for condition in pilot['conditions']:
                    new_pilot[0].conditions.add(Condition.objects.get(name=condition))

    def rollback_pilots(self):
        pass

    def load_upgrades(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        Upgrade = models.Upgrade 
        GrantsSlot = models.GrantsSlot
        Ship = models.Ship
        Condition = models.Condition
        Faction = models.Faction
        Slot = models.Slot
        Size = models.Size
        Action = models.Action

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
                        'slot': Slot.objects.get(name=upgrade['slot']),
                        'slot_cost': 1,
                        'points': upgrade['points'],
                        'attack': upgrade['attack'] if 'attack' in upgrade else None,
                        'range': upgrade['range'] if 'range' in upgrade else "",
                        'text': upgrade['text'],
                        'image': upgrade['image'] if 'image' in upgrade else "",
                        'xws': upgrade['xws'],
                        'unique': bool(upgrade['unique']) if 'unique' in upgrade else False,
                        'effect': upgrade['effect'] if 'effect' in upgrade else "",
                        'faction': Faction.objects.get(name=upgrade['faction']) if 'faction' in upgrade else None,
                        'limited': bool(upgrade['limited']) if 'limited' in upgrade else False,
                        'energy': upgrade['energy'] if 'energy' in upgrade else None,
                        'grants_attack': grants_stat['attack'] if 'attack' in grants_stat else None,
                        'grants_agility': grants_stat['agility'] if 'agility' in grants_stat else None,
                        'grants_hull': grants_stat['hull'] if 'hull' in grants_stat else None,
                        'grants_shields': grants_stat['shields'] if 'shields' in grants_stat else None,
                        'grants_skill': grants_stat['skill'] if 'skill' in grants_stat else None,})
            new_upgrade[0].grants_slot.clear()
            new_upgrade[0].grants_action.clear()
            if 'grants' in upgrade:
                for grant in upgrade['grants']:
                    if grant['type'] == "slot":
                        slot = grant['name']
                        GrantsSlot.objects.update_or_create(upgrade=new_upgrade[0], slot=Slot.objects.get(name=slot), defaults={
                            'quantity': GrantsSlot.objects.filter(upgrade=new_upgrade[0], slot=Slot.objects.get(name=slot)).count() + 1,})
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

    def rollback_upgrades(self):
        pass

    def load_reference_cards(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        ReferenceCard = models.ReferenceCard

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

    def rollback_reference_cards(self):
        pass

    def load_sources(self):
        schema_editor = connection.schema_editor()
        db_alias = schema_editor.connection.alias
        Source = models.Source
        Ship = models.Ship
        Pilot = models.Pilot
        Upgrade = models.Upgrade
        ReferenceCard = models.ReferenceCard
        Condition = models.Condition
        SourceShip = models.SourceShip
        SourcePilot = models.SourcePilot
        SourceUpgrade = models.SourceUpgrade

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

    def rollback_sources(self):
        pass

    def handle(self, *args, **options):
        # Rollback first to clear down the database
        self.rollback_definitions()
        self.rollback_ships()
        self.rollback_conditions()
        self.rollback_pilots()
        self.rollback_upgrades()
        self.rollback_reference_cards()
        self.rollback_sources()
        
        # Load the data
        self.load_definitions()
        self.load_ships() 
        self.load_conditions()
        self.load_pilots()
        self.load_upgrades()
        self.load_reference_cards() 
        self.load_sources()

