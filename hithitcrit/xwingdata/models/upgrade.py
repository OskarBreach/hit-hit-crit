from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

from .definition import Action, Faction, Size, Slot
from .ship import Ship
from .condition import Condition

class Upgrade(models.Model):
    name = models.CharField(max_length=30)
    """The upgrade's name as written on the card."""
    id = models.IntegerField(unique=True, primary_key=True, validators=[MinValueValidator(0)])
    """The upgrade's unique id number. It's not used in the game but it's used to link this upgrade to other data in this dataset."""
    slot = models.ForeignKey(Slot)
    """The slots type used by this upgrade."""
    slot_cost = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    """Number of slots required to equip this upgrade"""
    points = models.IntegerField(null=False)
    """Squad points cost for this upgrade."""
    attack = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """The upgrade's attack value."""
    range = models.CharField(max_length=255, blank=True, validators=[RegexValidator(regex='^[1-5](-[1-5])?$')])
    """The upgrade's range. Usually attack related."""
    text = models.CharField(max_length=512)
    """The upgrade's text as written on the card."""
    image = models.ImageField(upload_to="upgrade/", blank=True)
    """The file path for this upgrade's image."""
    xws = models.CharField(max_length=255)
    """The upgrade's unique XWS id as described in the XWS format."""
    unique = models.BooleanField(default=False)
    """Some upgrade cards have unique names, which are identified by the bullet to the left of the name.
    A player cannot field two or more cards that share the same unique name, even if those cards are of different types.
    """
    size = models.ManyToManyField(Size)
    """The ship sizes this upgrade is restricted to."""
    effect = models.CharField(max_length=255)
    """Some upgrades have effects, like bomb tokens.
    The text for such effects go here."""
    faction = models.ForeignKey(Faction, null=True, blank=True)
    """The factions this upgrade is restricted to."""
    limited = models.BooleanField(default=False)
    """Indicates if this upgrade has the Limited trait.
    A ship cannot equip more than one copy of the same card with the Limited trait.
    """
    energy = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    """The upgrade's energy cost"""
    grants_attack = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """Attack bonus granted by this upgrade"""
    grants_agility = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """Agility bonus granted by this upgrade"""
    grants_hull = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """Hull bonus granted by this upgrade"""
    grants_shields = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """Shield bonus granted by this upgrade"""
    grants_skill = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)]) 
    """Skill bonus granted by this upgrade"""
    grants_slot = models.ManyToManyField(Slot, through='GrantsSlot', related_name='grants') 
    """The slots granted by this upgrade"""
    grants_action = models.ManyToManyField(Action) 
    """The actions granted by this upgrade"""
    ship = models.ManyToManyField(Ship, blank=True)
    """The ships this upgrade is restricted to."""
    conditions = models.ManyToManyField(Condition, blank=True)
    """The upgrades's related conditions."""

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'faction',)

class GrantsSlot(models.Model):
    upgrade = models.ForeignKey(Upgrade)
    slot = models.ForeignKey(Slot)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        if self.quantity > 1:
            return "{0}: {1} (x{2})".format(self.upgrade, self.slot, self.quantity)
        else:
            return "{0}: {1}".format(self.upgrade, self.slot)

    class Meta:
        unique_together = ('upgrade', 'slot', )
