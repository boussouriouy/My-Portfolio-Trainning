from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def home(request):
    obj = Portfolio.objects.all()
    context = {
      'potfolio_items':obj 
    }
    return render(request, 'home.html', context)


