from django.shortcuts import get_object_or_404, redirect, render
from .forms import BotanicalForm
from .models import BotanicalRegister

def create(request):
    if request.method == 'POST':
        form = BotanicalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = BotanicalForm()
    return render(request, 'core/register_botanical.html', {'form': form, 'is_update': False })

def read(request):
    botanicals = BotanicalRegister.objects.all()
    return render(request, 'core/catalog.html', {'botanicals': botanicals})


def update(request, id):
    plant = get_object_or_404(BotanicalRegister, id=id)

    if request.method == 'POST':
        form = BotanicalForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = BotanicalForm(instance=plant)

    return render(request, 'core/register_botanical.html', {
        'form': form,
        'is_update': True,
        'plant': plant
    })

def delete(request, id):
    plant = get_object_or_404(BotanicalRegister, id=id)
    plant.delete()
    return redirect('catalog')

def view(request, id):
    plant = get_object_or_404(BotanicalRegister, id=id)
    return render(request, 'core/view_botanical.html', {'plant': plant})
