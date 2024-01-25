from django.contrib.auth.models import User
from django.db import models
from main.models import BaseModel
from django.utils.translation import gettext as _
from .data import organization_choices


class OrganizationModel(BaseModel):
    XK0YR2 = models.CharField(verbose_name=_("organization name"), max_length=6,
                              choices=organization_choices)
    HvQp14 = models.CharField(verbose_name=_("organization code"), max_length=6,
                              choices=organization_choices)
    hwUOSG = models.OneToOneField(User, on_delete=models.CASCADE, related_name='QmnECO')

    def __str__(self):
        return self.XK0YR2
