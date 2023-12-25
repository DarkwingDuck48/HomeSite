from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return render(request, "base/index.html")
    return redirect('users:login_user')
