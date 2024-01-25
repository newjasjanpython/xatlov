from django.forms import ModelForm
from .models import AppealSheetModel, ProblemSheetModel, MembersInForeignModel, MembersInSomeNotebookModel



class AppealSheetForm(ModelForm):
    class Meta:
        model = AppealSheetModel
        fields = "__all__"
    
    def save(self, mfy, district):
        ins = super().save(False)
        
        ins.cAdagL = mfy
        ins.fA0b7j = district
        
        ins.save()
        
        return ins


class ProblemSheetForm(ModelForm):
    class Meta:
        model = ProblemSheetModel
        fields = ['mStccp', 'dPmVJI', 'jZ4ndH']


class MembersInForeignForm(ModelForm):
    class Meta:
        model = MembersInForeignModel
        fields = ['jqfJ4u', 'GWUmHY', 'KzVEbd']


class MembersInSomeNotebookForm(ModelForm):
    class Meta:
        model = MembersInSomeNotebookModel
        fields = ['A3TP8D', 'aiJCTv']
