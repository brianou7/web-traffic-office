from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View


class AuthView(View):

    def get(self, request):
        return render(request, 'auth/sign-in.html', {})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('violations:index')

        return render(request, 'auth/sign-in.html', {'errors': form.errors})


def logout_view(request):
    logout(request)
    return redirect('violations:index')
