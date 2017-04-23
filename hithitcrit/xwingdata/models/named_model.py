from django.db import models
from django.core.validators import RegexValidator
from re import sub

class NamedModel(models.Model):
    """Fields used by all named models, regardless of type."""

    name = models.CharField(max_length=255)
    """The model's name as written on the cardi/ship itself."""
    url_name = models.CharField(max_length=255, validators=[RegexValidator(regex='^[a-z0-9\-]+$')])
    """The model's name used for hyperlinks."""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if getattr(self, 'name_changed', True):
            self.url_name = sub(r' +', '-', sub(r'[^a-z0-9]', ' ', self.name.lower()).strip())
        super(NamedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
