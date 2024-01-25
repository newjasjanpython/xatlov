from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import gettext as _
from main.models.problem_model import ProblemSheetModel
from cadmin.helps import get_filter_keys, get_page_color


class IndexView(View):
    def get(self, request):
        filters = {}
        page_color = 'primary'
        filter_name = "all"
        if not request.GET.get('no_filter') and request.GET.get('filter'):
            filters = get_filter_keys(request.GET.get('filter'))
            page_color = get_page_color(request.GET.get('filter'))
            filter_name = request.GET.get('filter').replace('-', ' ')
        user_code = str(request.user.QmnECO.HvQp14)
        filters['dgWV6p__isnull'] = False
        filters['Ue07qV'] = user_code
        context = {
            'select_key_name': _(filter_name),
            'objects': list(ProblemSheetModel.objects.filter(**filters)),
            'page_color': page_color
        }
        return render(request, 'orgadmin/index.html', context)
