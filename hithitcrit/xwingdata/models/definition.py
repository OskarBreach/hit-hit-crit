from django.db import models

class PrimaryFaction(models.Model):
    primary_faction = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.primary_faction

class Faction(models.Model):
    faction = models.CharField(max_length=255, unique=True)
    primary_faction = models.ForeignKey(PrimaryFaction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="factions/", blank=True)

    def __str__(self):
        return self.faction

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

class Slot(models.Model):
    slot = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.slot
