from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .definition import Action, Faction, Bearing, Difficulty, Size

class Ship(models.Model):
    """Fields used by all ships, regardless of size."""

    name = models.CharField(max_length=255, unique=True)
    """The ship's name as written on the card itself."""
    faction = models.ManyToManyField(Faction)
    """A list of factions this ship belongs to."""
    attack = models.IntegerField(blank=True, null=True, default=0, validators=[MinValueValidator(0)])
    """The ship's attack value."""
    agility = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    """The ship's agility value."""
    hull = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    """The ship's hull value."""
    shields = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    """The ship's shields value."""
    actions = models.ManyToManyField(Action, blank=True)
    """A list of all the actions the ship is capable of."""
    xws = models.CharField(max_length=255, unique=True)
    """The ship's unique XWS id as described in the XWS format."""
    id = models.IntegerField(unique=True, primary_key=True)
    """The ship's unique id number. It's not used in the game but it's used to link this ship to other data in this dataset."""
    maneuvers = models.ManyToManyField(Bearing, through='Dial')
    """The huge ship's maneuvers."""
    size = models.ForeignKey(Size)
    """The ship's size."""
    energy = models.IntegerField(blank=True, null=True, default=1, validators=[MinValueValidator(1)])
    """The ship's energy value."""
    epic_points = models.DecimalField(blank=True, null=True, default=0, decimal_places=1, max_digits=2, validators=[MinValueValidator(0)])
    """The ship's epic points value, as described in the X-Wing Epic Play Tournament Rules."""

    def __str__(self):
        return self.name

class Dial(models.Model):
    ship = models.ForeignKey(Ship)
    speed = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    bearing = models.ForeignKey(Bearing)
    difficulty = models.ForeignKey(Difficulty)
    maneuvers_energy = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0)])
    #TODO: Add validator to check maneuvers_energy is always defined for huge ships and never otherwise
    #TODO: Add validator to check difficuly is always white for huge ships

    def __str__(self):
        return "{0} {1} {2} ({3})".format(self.ship, self.speed, self.bearing, self.difficulty)

    class Meta:
        unique_together = ('ship', 'speed', 'bearing')
