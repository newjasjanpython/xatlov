from django.db import models
from django.utils.translation import gettext as _
from .base_model import BaseModel


class MembersInForeignModel(BaseModel):
    jqfJ4u = models.CharField(verbose_name=_("fullname of civil"), max_length=256)
    GWUmHY = models.DateField(verbose_name=_("birthday of civil"))
    KzVEbd = models.TextField(verbose_name=_("purpose for being in foreign"))

    def __str__(self) -> str:
        return f"{self.jqfJ4u}: Сабаби ({self.KzVEbd[:25]}) {self.GWUmHY}"

