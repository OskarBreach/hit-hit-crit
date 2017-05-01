from django.db import models

from .named_model import NamedModel

class PrimaryFaction(NamedModel):
    class Meta:
        unique_together = ('name',)

class Faction(NamedModel):
    primary_faction = models.ForeignKey(PrimaryFaction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="factions/", blank=True)

    class Meta:
        unique_together = ('name',)

class Size(models.Model):
    size = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.size

class Action(models.Model):
    action = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.action

class Bearing(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    #TODO: restrictions on speed (add Template class?)

    def __str__(self):
        return self.name

class Difficulty(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "difficulties"

class Slot(NamedModel):
    class Meta:
        unique_together = ('name',)
