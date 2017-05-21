from django.db import models
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

class ReferenceCard(models.Model):
    """Schema for reference card data file"""

    id = models.IntegerField(unique=True, primary_key=True, validators=[MinValueValidator(0)])
    """The reference card's unique id number. It's not used in the game but it's used to link this reference card to other data in this dataset."""
    title = models.CharField(max_length=255)
    """The reference card's title as written on the card itself."""
    subtitle = models.CharField(max_length=255)
    """The reference card's subtitle as written on the card itself."""
    image = models.ImageField(upload_to="reference-cards/", blank=True)
    """The file path for this reference card's image."""
    text = models.CharField(max_length=255)
    """The reference card's text describing or updating new rules."""
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify("{0}-{1}".format(self.title, self.subtitle))
        super(ReferenceCard, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('reference-card-details', kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('title', 'subtitle',)
