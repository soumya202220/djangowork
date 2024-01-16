from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')

def log(request):
    return render(request, 'log.html')
        
