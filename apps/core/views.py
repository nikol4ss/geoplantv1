from django.shortcuts import render, redirect
from .forms import BotanicalForm

def create_botanical(request):
    if request.method == 'POST':
        form = BotanicalForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BotanicalForm()
    return render(request, 'core/register_botanical.html', {'form': form})
