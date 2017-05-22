from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class PrimaryFaction(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PrimaryFaction, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('primary-faction-details', kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('name',)

class Faction(models.Model):
    name = models.CharField(max_length=255)
    primary_faction = models.ForeignKey(PrimaryFaction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="factions/", blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Faction, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('faction-details', kwargs={"slug": self.slug})

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
    name = models.CharField(max_length=255, unique=True)
    #TODO: restrictions on speed (add Template class?)

    def __str__(self):
        return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "difficulties"

class Slot(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Slot, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('slot-details', kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('name',)
