from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from owners.models import Owner
from owners.forms import OwnerForm


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


class SignUpView(View):

    context = {
        'types': Owner.TYPES,
        'id_types': Owner.ID_TYPES,
    }

    def get(self, request):
        return render(request, 'auth/sign-up.html', self.context)

    def post(self, request):
        form = OwnerForm(data=request.POST)

        if form.is_valid():
            form.save()
            user = form.instance
            user.set_password(form.cleaned_data['password'])
            user.save(force_update=True)
            login(request, user)
            return redirect('violations:index')

        context = self.context | {'errors': form.errors}
        return render(request, 'auth/sign-up.html', context)


def logout_view(request):
    logout(request)
    return redirect('violations:index')
