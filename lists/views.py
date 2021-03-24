from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("Hello, world. You're at the list homepage.")
