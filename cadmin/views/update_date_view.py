from django.views.generic import View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from main.models.problem_model import ProblemSheetModel


class UpdateDateView(View):
    def post(self, request):
        object_ = get_object_or_404(ProblemSheetModel, pk=request.POST.get('object_pk'))
        data = {
            'status': 'success',
            'detail': f'Updated date for {request.POST.get("object_pk")}',
            'data': {'update': True}
        }

        if 'new_date' in request.POST.keys():
            try:
                object_.dgWV6p = str(request.POST.get('new_date')).replace('/', '-')
                object_.x2tBdd = 413
                object_.save()
            except:
                data = {
                    'status': 'fail',
                    'detail': f'Updated date for {request.POST.get("object_pk")}',
                    'data': {'update': False}
                }
        return JsonResponse(data)
