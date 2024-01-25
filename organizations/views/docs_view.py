from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import error
from django.utils.translation import gettext as _
from main.models.problem_model import ProblemSheetModel


class DocsView(View):
    def get(self, request, pk):
        before_title = request.GET.get('before_title', _("all"))
        before_url = request.GET.get('before_url', _("/organization/?no_filter=1"))
        user_code = str(request.user.QmnECO.HvQp14)
        object_ = get_object_or_404(ProblemSheetModel, pk=pk)

        if str(object_.Ue07qV) != user_code:
            error(request, _("this is not your type"))
            return redirect('/organization/')

        context = {
            'object': object_,
            'before_title': before_title,
            'before_url': before_url
        }
        return render(request, 'orgadmin/docs.html', context)
