from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {
        'page': request.path
    }
    return render(request, 'supplychain/welcome.html', context)

