from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from .definition import Faction, Slot
from .ship import Ship
from .condition import Condition

class Pilot(models.Model):
    """Schema for pilots data file"""

    name = models.CharField(max_length=255)
    """The pilot's name, as written on the card itself."""
    id = models.IntegerField(unique=True, primary_key=True, validators=[MinValueValidator(0)])
    """The pilot's unique id number. It's not used in the game but it's used to link this pilot to other data in this dataset."""
    unique = models.BooleanField(default=False)
    """Indicates whether this pilot has a unique name or not.
    Some pilot cards have unique names, which are identified by the bullet to the left of the name.
    A player cannot field two or more cards that share the same unique name, even if those cards are of different types.
    """
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    """The pilot's ship name."""
    skill = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    """The pilot's skill."""
    skill_special_ruling = models.BooleanField(default=False)
    """Having '?' as a pilot's skill means that there is a special ruling for it and it's variable."""
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    """This pilot's squad points cost."""
    points_special_ruling = models.BooleanField(default=False)
    """Having '?' as a pilot's squad points cost means that there is a special ruling for it and it's variable."""
    slots = models.ManyToManyField(Slot, through='PilotSlot')
    """A list of the slots available to this pilot."""
    text = models.CharField(max_length=255, blank=True)
    """The pilot card's text describing its effect."""
    image = models.ImageField(upload_to="pilots/", blank=True)
    "The file path for this pilot card's image."
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    """The pilot's faction."""
    xws = models.CharField(max_length=255)
    """The pilot's unique XWS id as described in the XWS format."""
    attack_override = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0)])
    """The ship's attack value."""
    agility_override = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0)])
    """The ship's agility value."""
    hull_override = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0)])
    """The ship's hull value."""
    shields_override = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0)])
    """The ship's shields value."""
    range = models.CharField(max_length=255, blank=True, validators=[RegexValidator(regex='^[1-5](-[1-5])?$')])
    """The ship's range. This property is for huge ships only."""
    conditions = models.ManyToManyField(Condition, blank=True)
    """The pilot's related conditions."""

    def __str__(self):
        return "{0} {1} {2} ({3})".format(self.faction, self.ship, self.name, self.xws)

    class Meta:
        unique_together = ('ship', 'faction', 'xws',)

class PilotSlot(models.Model):
    pilot = models.ForeignKey(Pilot)
    slot = models.ForeignKey(Slot)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        if self.quantity > 1:
            return "{0}: {1} (x{2})".format(self.pilot, self.slot, self.quantity)
        else:
            return "{0}: {1}".format(self.pilot, self.slot)

    class Meta:
        unique_together = ('pilot', 'slot', )
