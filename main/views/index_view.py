from django.views.generic import View
from django.shortcuts import render, redirect
from ..forms import AppealSheetForm


class IndexView(View):
    def get(self, request):
        L5lfny = AppealSheetForm()

        unepv0 = {
            "XWeJMr": L5lfny
        }

        return render(request, 'users/index.html', unepv0)

    def post(self, request):
        mfy = request.user.mfymodel
        district = mfy.KFA1gv
        
        L5lfny = AppealSheetForm(request.POST)
        if L5lfny.is_valid():
            L5lfny.save(mfy, district)
            return redirect('/')

        unepv0 = {
            "XWeJMr": L5lfny
        }

        return render(request, 'users/index.html', unepv0)
