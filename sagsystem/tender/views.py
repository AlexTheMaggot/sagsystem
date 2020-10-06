from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenderForm, ProductForm
from .models import Tender, Product, Provider, Goods
from mainapp.models import Measure


def tenders(request):
    tenders_list = Tender.objects.all()
    context = {
        'tenders': tenders_list
    }
    return render(request, 'tender/tenders.html', context)


def tender_detail(request, id):
    tender = get_object_or_404(Tender, id__exact=id)
    context = {
        'tender': tender,
    }
    return render(request, 'tender/tender_detail.html', context)


def new_tender(request):
    return render(request, 'tender/new_tender.html')


def tender_add(request):
    if request.method == 'POST':
        form = TenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenders')
    return redirect('new_tender')


def tender_delete(request, id):
    tender = Tender.objects.get(id=id)
    tender.delete()
    return redirect('tenders')


def product_list(request):
    products = Product.objects.all().order_by('name')
    context = {
        'products': products,
    }
    return render(request, 'tender/product_list.html', context)


def product_add(request):
    measures = Measure.objects.all().order_by('name')

    context = {
        'measures': measures,
    }
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tender/products/')
    return render(request, 'tender/product_add.html', context)


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/tender/products')


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    measures = Measure.objects.all().order_by('name')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/tender/products')

    context = {
        'product': product,
        'measures': measures,
    }
    return render(request, 'tender/product_edit.html', context)


def provider_list(request):
    providers = Provider.objects.all()
    context = {
        'providers': providers,
    }
    return render(request, 'tender/provider_list.html', context)
