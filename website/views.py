from django.shortcuts import render
from website.models import MyApp

# Create your views here.


def index(request):
    # model.objects.command is creating a query (like SQL)
    all_apps = MyApp.objects.all()

    # Dictionary with key values
    context = {
        'my_apps': all_apps,
        'app_name': request.resolver_match.app_name
    }
    # Query passed as context  below
    return render(request, 'website/index.html', context)


def samples(request):
    return render(request, 'website/samples.html', )
