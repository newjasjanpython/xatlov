from django.views.generic import View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from main.forms import ProblemSheetForm
from main.models import ProblemSheetModel


class ProblemCreateApi(View):
    def post(self, request):
        form = ProblemSheetForm(request.POST)
        if form.is_valid():
            i = form.save()
            return JsonResponse({"status": "success", "detail": "Create problem", "id": i.pk})
        return JsonResponse({"status": "error", "detail": "Missing data", "errors": form.errors.as_json()}, status=500)


class ProblemEditApi(View):
    def post(self, request):
        instance = get_object_or_404(ProblemSheetModel, pk=request.POST.get('id'))
        form = ProblemSheetForm(request.POST, instance=instance)
        if form.is_valid():
            i = form.save()
            return JsonResponse({"status": "success", "detail": "Updated problem", "id": i.pk})
        return JsonResponse({"status": "error", "detail": "Missing data", "errors": form.errors.as_json()}, status=500)
