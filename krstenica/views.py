from django.shortcuts import render, redirect
from .models import krsteni_list
from .forms import krsteni_listForm
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = krsteni_listForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Крштени лист је сачуван!')
            return redirect('list')
    form = krsteni_listForm

    page = {
        'forms': form,
    }
    return render(request, 'krstenica/index.html', page)
