from django.contrib.auth.models import User
from django.db import models
from main.models import BaseModel
from django.utils.translation import gettext as _


class DistrictModel(BaseModel):
    MuEJnH = models.CharField(verbose_name=_("district name"), max_length=50)
    Ay7vlW = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.MuEJnH


class MfyModel(BaseModel):
    KFA1gv = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    A3EIK9 = models.PositiveIntegerField(verbose_name=_("sector number"))
    OJkwnh = models.CharField(verbose_name=_("mfy name"), max_length=50)
    YAWyKM = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.OJkwnh
