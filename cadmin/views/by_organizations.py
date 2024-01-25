from django.shortcuts import render
from django.views.generic import View
from main.models.problem_model import ProblemSheetModel
from ..data import codes_with_icons
from ..helps import get_filter_keys


# Create your views here.


class ByOrganizationsView(View):
    def get(self, request):
        code = request.GET.get('code_query', '1.')

        context = {
            'codes': codes_with_icons,
            'filter': {
                'code': code,
                'all': {
                    'count': ProblemSheetModel.objects.filter(Ue07qV=code).count()
                },
                'on_progress': {
                    'count': ProblemSheetModel.objects.filter(**get_filter_keys('on-progress'), Ue07qV=code).count()
                },
                'finished': {
                    'count': ProblemSheetModel.objects.filter(**get_filter_keys('finished'), Ue07qV=code).count()
                },
                'over_deadline': {
                    'count': ProblemSheetModel.objects.filter(**get_filter_keys('over-deadline'), Ue07qV=code).count()
                }
            }
        }
        return render(request, 'admins/by_organizations.html', context)
