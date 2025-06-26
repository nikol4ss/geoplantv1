from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import BotanicalForm
from .models import BotanicalRegister

@never_cache
@login_required
def create(request):
    if request.method == 'POST':
        form = BotanicalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = BotanicalForm()
    return render(request, 'core/register_botanical.html', {'form': form, 'is_update': False })

@never_cache
@login_required
def read(request):
    botanicals = BotanicalRegister.objects.all()
    return render(request, 'core/catalog.html', {'botanicals': botanicals})

@never_cache
@login_required
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

@never_cache
@login_required
def delete(request, id):
    plant = get_object_or_404(BotanicalRegister, id=id)
    plant.delete()
    return redirect('catalog')

@never_cache
@login_required
def view(request, id):
    plant = get_object_or_404(BotanicalRegister, id=id)
    return render(request, 'core/view_botanical.html', {'plant': plant})
