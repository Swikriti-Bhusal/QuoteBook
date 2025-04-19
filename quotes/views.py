from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm
def home(request):
    quotes=Quote.objects.all()
    form = QuoteForm(request.POST or None, request.FILES or None)


    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    
    
    return render(request, 'quotes/home.html' , {'quotes': quotes, 'form': form})

