from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

from .ship import Ship
from .pilot import Pilot
from .upgrade import Upgrade
from .reference_card import ReferenceCard
from .condition import Condition

class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)
    """The source's name as written on the package."""
    id = models.IntegerField(unique=True, primary_key=True, validators=[MinValueValidator(0)])
    """The source's unique id number. It's not used in the game but it's used to link this source to other data in this dataset."""
    image = models.ImageField(upload_to="sources/", blank=True)
    """The file path for this pilot card's image."""
    thumb = models.ImageField(upload_to="sources/", blank=True)
    """The file path for this source's thumbnail."""
    wave = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    """The sources wave (or product line)."""
    special_wave_name = models.CharField(null=True, blank=True, max_length=255)
    """Some sources are not grouped under particular wave, but under a particular product line
       When that's the case, use text for that type."""
    released = models.BooleanField(default=False)
    """This value indicates whether this sources has been released or not."""
    sku = models.CharField(unique=True, max_length=100, validators=[RegexValidator('^SWX[0-9]+$')])
    """Fantasy Flight Games unique product key for this particular source."""
    announcement_date = models.DateField()
    """Indicates the date on which the source was announced."""
    release_date = models.DateField(blank=True, null=True)
    """Indicates the date on which the source was released."""
    slug = models.SlugField(unique=True)
    
    """Contents"""
    ships = models.ManyToManyField(Ship, through='SourceShip')
    pilots = models.ManyToManyField(Pilot, through='SourcePilot')
    upgrades = models.ManyToManyField(Upgrade, through='SourceUpgrade')
    reference_cards = models.ManyToManyField(ReferenceCard, blank=True)
    conditions = models.ManyToManyField(Condition, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Source, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('source-details', kwargs={"slug": self.slug})

class SourceShip(models.Model):
    source = models.ForeignKey(Source)
    ship = models.ForeignKey(Ship)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        if self.quantity > 1:
            return "{0}: {1} (x{2})".format(self.source, self.ship, self.quantity)
        else:
            return "{0}: {1}".format(self.source, self.ship)

    class Meta:
        unique_together = ('source', 'ship')

class SourcePilot(models.Model):
    source = models.ForeignKey(Source)
    pilot = models.ForeignKey(Pilot)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        if self.quantity > 1:
            return "{0}: {1} (x{2})".format(self.source, self.pilot, self.quantity)
        else:
            return "{0}: {1}".format(self.source, self.pilot)

    class Meta:
        unique_together = ('source', 'pilot')

class SourceUpgrade(models.Model):
    source = models.ForeignKey(Source)
    upgrade = models.ForeignKey(Upgrade)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        if self.quantity > 1:
            return "{0}: {1} (x{2})".format(self.source, self.upgrade, self.quantity)
        else:
            return "{0}: {1}".format(self.source, self.upgrade)

    class Meta:
        unique_together = ('source', 'upgrade')
