from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import gettext as _
from ..helps import get_page_color, get_list_sectors


class ListProblems(View):
    def get(self, request):
        code = request.GET.get('code')
        page_name = "all"
        if not code:
            return redirect('/admin/')
    
        if 'filter' in request.GET.keys():
            filters = request.GET.get('filter')
            page_color = get_page_color(request.GET.get('filter'))
            page_name = request.GET.get('filter').replace('-', ' ')
        else:
            filters = None
            page_color = "primary"

        context = {
            'objects': get_list_sectors(filters, code),
            'page_code': page_color,
            'page_name': _(page_name)
        }

        return render(request, 'admins/list-objects.html', context)
