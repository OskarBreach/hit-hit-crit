from django.db import models
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

class Condition(models.Model):
    """Schema for conditions data file"""

    name = models.CharField(max_length=255)
    """The model's name as written on the card itself."""
    image = models.ImageField(upload_to="condition/", blank=True)
    """The file path for this condition card's image."""
    xws = models.CharField(max_length=255, unique=True)
    """The conditions's unique XWS id as described in the XWS format."""
    text = models.CharField(max_length=512)
    """The condition card's text describing its effect."""
    unique = models.BooleanField(default=False)
    """Some condition cards have unique names, which are identified by the bullet to the left of the name.
    A player cannot field two or more cards that share the same unique name, even if those cards are of different types.
    """
    id = models.IntegerField(unique=True, primary_key=True, validators=[MinValueValidator(0)])
    """The condition's unique id number. It's not used in the game but it's used to link this condition to other data in this dataset."""
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Condition, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('condition-details', kwargs={"slug": self.slug})
