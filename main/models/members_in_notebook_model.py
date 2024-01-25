from django.db import models
from django.utils.translation import gettext as _
from .base_model import BaseModel


class MembersInSomeNotebookModel(BaseModel):
    A3TP8D = models.CharField(verbose_name=_("fullname of civil"), max_length=256)
    aiJCTv = models.CharField(max_length=256, choices=(('metal', 'Темир дафтар'), ('famales', 'Аёллар дафтари'), ('youth', 'Ёшлар дафтари')))

    def __str__(self) -> str:
        return f"{self.A3TP8D}"
