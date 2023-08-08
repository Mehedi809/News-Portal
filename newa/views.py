from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    banner = Banner.objects.all()
    Bangladesh = Content.objects.filter(category__name = 'Bangladesh')
    International = Content.objects.filter(category__name = 'internations')
    Sports = Content.objects.filter(category__name = 'sports')
    Islam = Content.objects.filter(category__name = 'islam')

    
    context = {
        'banner': banner,
        'Bangladesh': Bangladesh,
        'International': International,
        'Sports': Sports,
        'Islam': Islam
        }
    return render(request, 'store/index.html', context)


# # def forms(request):
#     form = FormCreate
#     if request.method == 'POST':
#         form = FormCreate(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'You are success')
#             return redirect('/')
#     context = {
#         'form': form
#     }
#     return render(request, 'store/forms.html', context)
    


