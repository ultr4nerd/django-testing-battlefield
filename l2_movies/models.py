"""Movies level app models"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    """Movie model"""
    name = models.CharField(_("name"), max_length=255)
    director = models.ForeignKey(
        verbose_name=_("director"),
        to="Director",
        on_delete=models.CASCADE,
    )
    date = models.DateField(_("date"))

    def __str__(self) -> str:
        """String representation of a movie"""
        return "{} ({})".format(self.name, self.date.year)


class Director(models.Model):
    """Director model"""
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    birthday = models.DateField(_("birthday"))

    def __str__(self) -> str:
        """String representation of a director"""
        return "{} {}".format(self.first_name, self.last_name)
