from django.db import models
from django.utils.translation import gettext as _
from .base_model import BaseModel
from .choices import wMTlNk
from .members_in_foreign_model import MembersInForeignModel
from .members_in_notebook_model import MembersInSomeNotebookModel
from .problem_model import ProblemSheetModel


class AppealSheetModel(BaseModel):
    cAdagL = models.ForeignKey('cadmin.MfyModel', on_delete=models.PROTECT, related_name='VXE6it', null=True, blank=True)
    fA0b7j = models.ForeignKey('cadmin.DistrictModel', on_delete=models.PROTECT, related_name='XtYo0K', null=True, blank=True)

    sWqfd7 = models.DateField(auto_now_add=True) # Date this appeal hourse reserched
    OrTY1z = models.CharField(verbose_name=_("house address"), max_length=256)
    uhz0cN = models.CharField(verbose_name=_("house economic and social position"), max_length=256, choices=wMTlNk)

    NDoqjy = models.BooleanField(verbose_name=_("house problems"), default=False)

    hB7sSi = models.CharField(verbose_name=_("applicant fio"), max_length=256)
    pcPMf0 = models.DateField(verbose_name=_("applicant birthday"))
    MsaQKr = models.PositiveIntegerField(verbose_name=_("applicant gender"), choices=[(1, 'Эркак'), (2, 'Аёл')])
    lXV0Ax = models.CharField(verbose_name=_("applicant contact"), max_length=256)

    wplJMW = models.BooleanField(verbose_name=_("need energy efficient equipment"), default=False)
    Lwo3mi = models.PositiveIntegerField(verbose_name=_("energy efficient equipment installation budget"), choices=[(1, 'Ўз маблағига'), (2, 'Имтиёзли кредитга')], null=True, blank=True)
    kbuia9 = models.PositiveIntegerField(verbose_name=_("energy efficient equipment kw"), default=0)

    wLVuSe = models.BooleanField(verbose_name=_("request for a loan"), default=False)
    VANCTz = models.PositiveBigIntegerField(verbose_name=_("load sum paid"), default=0)
    OA0yaU = models.PositiveIntegerField(verbose_name=_("requester gender"), choices=((1, 'Аёллар'), (2, 'Ёшлар')), null=True, blank=True)
    kYeOx4 = models.TextField(verbose_name=_("request purpose"), null=True, blank=True)

    V0djcq = models.BooleanField(verbose_name=_("demand subsidy"), default=False)
    kwsAGh = models.PositiveIntegerField(verbose_name=_("demanding gender"), choices=((1, 'Аёллар'), (2, 'Ёшлар')), null=True, blank=True)
    quTj0L = models.TextField(verbose_name=_("demand purpose"), max_length=256, blank=True, null=True)

    L3iXGb = models.ManyToManyField(MembersInForeignModel, blank=True)
    m9GgHo = models.ManyToManyField(ProblemSheetModel, blank=True, related_name="n4jAme")
    d0Gawy = models.ManyToManyField(MembersInSomeNotebookModel, blank=True)
    
    def __str__(self):
        return f"<Appeal fio={self.hB7sSi} birth_date={self.pcPMf0} contact={self.lXV0Ax}>"
