from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name,
    }
    return render(request, 'supplychain/welcome.html', context)

def upload_file(request):
    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'File uploaded successfully!'
    }
    return render(request, 'supplychain/welcome.html', context)
