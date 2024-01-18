import django.apps.registry as app_registry
from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        APPS = app_registry.apps.get_app_configs()
        custom_install_apps = {}
        for app in APPS:
            try:
                if app.homesite_application: # type: ignore Custom Fields for application
                    if not app.homesite_tech_application: # type: ignore Custom Fields for application
                        custom_install_apps.update({app.name: app})
            except AttributeError:
                print(app.name)
            print(app)
        context = {"custom_applications": custom_install_apps}
        return render(request, "base/index.html", context)
    return redirect('users:login_user')
