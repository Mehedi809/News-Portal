from django.shortcuts import render, redirect
from newa.models import *
from .forms import *

# Create your views here.
def dashboard_home(request):
    banner = Banner.objects.all()
    content = Content.objects.all()
    
    context={
        'banner': banner,
        'article': content,
    }
    return render(request, 'crudeapi/dashboard.html', context)


def BannerAdd(request):
    form = BannerForm()
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('dashboard_home')
    context = {
        'form': form
    }
    return render(request, 'crudeapi/banner-add.html', context)


def BannerView(request, pk):
    banner = Banner.objects.get(pk=pk)
    context = {
        'banner': banner
    }
    return render(request, 'crudeapi/banner-view.html', context) 


def BannerEdit(request, title):
    banner = Banner.objects.get(title=title)
    form = BannerForm(instance=banner)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid:
            form.save()
            return redirect('dashboard_home')
    context = {
        'form': form
    }
    return render(request, 'crudeapi/banner-add.html', context)


def BannerDelete(request, pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('dashboard_home')


def ArticleAdd(request):
    form = ContentForm()
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('dashboard_home')
    context = {
        'form': form
    }
    return render(request, 'article/ArticleAdd.html', context)


def ArticleView(request, pk):
    article = Content.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'article/article-view.html', context) 


def ArticleEdit(request, title):
    article = Content.objects.get(title=title)
    form = ContentForm(instance=article)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
            return redirect('dashboard_home')
    context = {
        'form': form
    }
    return render(request, 'article/ArticleAdd.html', context)


def ArticleDelete(request, pk):
    article = Content.objects.get(pk=pk)
    article.delete()
    return redirect('dashboard_home')


