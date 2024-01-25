from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.messages import error, success
from django.utils.translation import gettext as _
from main.models.problem_model import ProblemSheetModel
import datetime


class DocsReplyView(View):
    def get(self, request, pk):
        user_code = str(request.user.QmnECO.HvQp14)
        object_ = get_object_or_404(ProblemSheetModel, pk=pk)

        if str(object_.Ue07qV) != user_code:
            error(request, _("this is not your type"))
            return redirect('/organization/')

        if not object_.dIyvXl:
            error(request, _("no reply found there"))
            return redirect('/organization/')

        context = {
            'before_title': request.GET.get('before_title', 'all'),
            'before_url': request.GET.get('before_url', '/organization/'),
            'object': object_
        }

        return render(request, 'orgadmin/docs_reply.html', context)

    def post(self, request, pk):
        reply_text = request.POST.get('dIyvXl')
        reply_file = request.FILES.get('vKlZ9t')

        if not (reply_text and reply_file):
            error(request, _("reply for appeal problem error"))
            return redirect('/organization/')

        user_code = str(request.user.QmnECO.HvQp14)
        object_ = get_object_or_404(ProblemSheetModel, pk=pk)

        if object_.dgWV6p < datetime.date.today():
            error(request, _("over deadline error"))
            object_.x2tBdd = 415
            object_.save()
            return redirect('/organization/')

        if str(object_.Ue07qV) != user_code and object_.x2tBdd != 213:
            error(request, _("this is not your type"))
            return redirect('/organization/')
        else:
            success(request, _("reply for appeal problem success"))
            object_.dIyvXl = reply_text
            object_.vKlZ9t = reply_file
            object_.x2tBdd = 416
            object_.save()

            return redirect(request.POST.get('next'))
