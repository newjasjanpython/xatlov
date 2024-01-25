from django.views.generic import View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from main.forms import MembersInForeignForm
from main.models import MembersInForeignModel


class MembersInForeignCreateApi(View):
    def post(self, request):
        form = MembersInForeignForm(request.POST)
        if form.is_valid():
            i = form.save()
            return JsonResponse({"status": "success", "detail": "Create problem", "id": i.pk})
        return JsonResponse({"status": "error", "detail": "Missing data", "errors": form.errors.as_json()}, status=500)


class MembersInForeignEditApi(View):
    def post(self, request):
        instance = get_object_or_404(MembersInForeignModel, pk=request.POST.get('id'))
        form = MembersInForeignForm(request.POST, instance=instance)
        if form.is_valid():
            i = form.save()
            return JsonResponse({"status": "success", "detail": "Updated problem", "id": i.pk})
        return JsonResponse({"status": "error", "detail": "Missing data", "errors": form.errors.as_json()}, status=500)
