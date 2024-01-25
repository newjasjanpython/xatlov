from django.shortcuts import render, redirect
from django.views.generic import View
from main.models.problem_model import ProblemSheetModel
from ..data import codes_with_icons
from ..helps import get_filter_keys, get_page_color
from django.utils.translation import gettext as _

# Create your views here.


class IndexView(View):
    def get(self, request):
        page_name = "all"
        if 'filter' in request.GET.keys():
            filters = get_filter_keys(request.GET.get('filter'))
            page_color = get_page_color(request.GET.get('filter'))
            page_name = request.GET.get('filter').replace('-', ' ')
        else:
            filters = {}
            page_color = 'primary'

        context = {
            'codes_with_icons': codes_with_icons,
            'counts_by_codes': [
                {
                    'data': i,
                    'objects': list(ProblemSheetModel.objects.filter(Ue07qV=i['code'], **filters))
                } for i in codes_with_icons
            ],
            'page_code': page_color,
            'page_name': _(page_name)
        }
        return render(request, 'admins/index.html', context)
