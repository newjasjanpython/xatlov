from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.messages import success, error
from django.utils.translation import gettext as _


class LoginView(View):
    def get(self, request):
        return render(request, 'admins/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user: User = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                success(request, _("logged in successfully"))
            else:
                error(request, _("password is incorrect"))
                return render(request, 'admins/login.html')
        except Exception as err:
            error(request, _("no such user with that username"))
            return render(request, 'admins/login.html')

        return redirect(request.POST.get('next') or '/admin/')
