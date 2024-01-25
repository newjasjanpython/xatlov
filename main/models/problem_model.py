from django.db import models
from django.utils.translation import gettext as _


class ProblemSheetModel(models.Model):
    mStccp = models.CharField(verbose_name=_("fullname of civil"), max_length=256)
    dPmVJI = models.DateField(verbose_name=_("birthday of civil"))
    jZ4ndH = models.TextField(verbose_name=_("appeal description or text"))
    Ue07qV = models.CharField(verbose_name=_("appeal level code"), max_length=256, null=True, blank=True)
    Cq04qZ = models.CharField(verbose_name=_("organization for appeal"), max_length=256, null=True, blank=True)
    dgWV6p = models.DateField(verbose_name=_("deadline for appeal"), null=True, blank=True)
    x2tBdd = models.PositiveIntegerField(verbose_name=_("appeal status"), default=412)

    dIyvXl = models.TextField(verbose_name=_("appeal solution thanks"), null=True, blank=True)
    vKlZ9t = models.FileField(verbose_name=_("appeal solution thanks [file]"), upload_to='pdf/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.mStccp} {self.jZ4ndH}"

    @property
    def x2tBdd_disp(self):
        if self.x2tBdd == 412:
            return _("no date given")
        elif self.x2tBdd == 413:
            return _("on progress")
        elif self.x2tBdd == 414:
            return _("finished")
        elif self.x2tBdd == 415:
            return _("over deadline")
        elif self.x2tBdd == 416:
            return _("for verify")
        return _("static status")
