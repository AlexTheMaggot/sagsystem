from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenderForm, ProductForm, ProductCategoryForm, ProviderForm, ParticipantForm, GoodsForm
from .models import Tender, Product, Provider, ProductCategory, Participant, Goods
from mainapp.models import Measure
from django_pandas.io import read_frame


def tender_list(request):
    tenders = Tender.objects.all().order_by('name')
    context = {
        'tenders': tenders,
    }
    return render(request, 'tender/tender_list.html', context)


def tender_detail(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    participants = Participant.objects.all().filter(tender_id__exact=tender_id)
    goods = Goods.objects.all().filter(tender_id__exact=tender_id)
    context = {
        'tender': tender,
        'participants': participants,
        'goods': goods,
    }
    if goods:
        rows = ['product__name']
        cols = ['participant__provider__name']
        fieldnames = ['product__name', 'price', 'participant__provider__name']

        df = goods.to_pivot_table(fieldnames=fieldnames, values='price',
                                  rows=rows, cols=cols, verbose=True)
        table = df.to_html(classes=['table', 'table-striped'])
        context['table'] = table
    return render(request, 'tender/tender_detail.html', context)


def tender_add(request):
    if request.method == 'POST':
        form = TenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tender/')
    return render(request, 'tender/tender_add.html')


def tender_delete(request, tender_id):
    provider = get_object_or_404(Tender, id=tender_id)
    provider.delete()
    return redirect('/tender/')


def tender_edit(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)

    if request.method == 'POST':
        form = TenderForm(request.POST, instance=tender)
        if form.is_valid():
            form.save()
            return redirect('/tender/')

    context = {
        'tender': tender,
    }
    return render(request, 'tender/tender_edit.html', context)


def product_list(request):
    products = Product.objects.all().order_by('name')
    categories = ProductCategory.objects.all().order_by('name')
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'tender/product_list.html', context)


def product_add(request):
    measures = Measure.objects.all().order_by('name')
    categories = ProductCategory.objects.all().order_by('name')

    context = {
        'measures': measures,
        'categories': categories,
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
    categories = ProductCategory.objects.all().order_by('name')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/tender/products')

    context = {
        'product': product,
        'measures': measures,
        'categories': categories,
    }
    return render(request, 'tender/product_edit.html', context)


def product_by_category(request, id):
    products = Product.objects.filter(category_id__exact=id).order_by('name')
    categories = ProductCategory.objects.all().order_by('name')
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'tender/product_list.html', context)


def product_category_list(request):
    product_categories = ProductCategory.objects.all().order_by('name')
    context = {
        'product_categories': product_categories,
    }
    return render(request, 'tender/product_category_list.html', context)


def product_category_add(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tender/product-category/')
    return render(request, 'tender/product_category_add.html')


def product_category_delete(request, id):
    product_category = get_object_or_404(ProductCategory, id=id)
    product_category.delete()
    return redirect('/tender/product-category/')


def product_category_edit(request, id):
    product_category = get_object_or_404(ProductCategory, id=id)

    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance=product_category)
        if form.is_valid():
            form.save()
            return redirect('/tender/product-category')

    context = {
        'product_category': product_category,
    }
    return render(request, 'tender/product_category_edit.html', context)


def provider_list(request):
    providers = Provider.objects.all().order_by('name')
    context = {
        'providers': providers,
    }
    return render(request, 'tender/provider_list.html', context)


def provider_detail(request, id):
    provider = get_object_or_404(Provider, id=id)

    context = {
        'provider': provider,
    }
    return render(request, 'tender/provider_detail.html', context)


def provider_add(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tender/providers/')
    return render(request, 'tender/provider_add.html')


def provider_delete(request, id):
    provider = get_object_or_404(Provider, id=id)
    provider.delete()
    return redirect('/tender/providers/')


def provider_edit(request, id):
    provider = get_object_or_404(Provider, id=id)

    if request.method == 'POST':
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('/tender/providers')

    context = {
        'provider': provider,
    }
    return render(request, 'tender/provider_edit.html', context)


def participant_add(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    providers = Provider.objects.all().order_by('name')
    context = {
        'tender': tender,
        'providers': providers,
    }
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            url = '/tender/' + str(tender.id) + '/'
            return redirect(url)
    return render(request, 'tender/participant_add.html', context)


def participant_detail(request, tender_id, participant_id):
    tender = get_object_or_404(Tender, id=tender_id)
    goods = Goods.objects.all().filter(participant_id__exact=participant_id)
    participant = get_object_or_404(Participant, id=participant_id)
    context = {
        'tender': tender,
        'participant': participant,
        'goods': goods,
    }
    return render(request, 'tender/participant_detail.html', context)


def participant_edit(request, tender_id, participant_id):
    tender = get_object_or_404(Tender, id=tender_id)
    participant = get_object_or_404(Participant, id=participant_id)
    providers = Provider.objects.all().order_by('name')
    context = {
        'tender': tender,
        'providers': providers,
        'participant': participant,
    }
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            url = '/tender/' + str(tender.id) + '/' + str(participant.id) + '/'
            return redirect(url)
    return render(request, 'tender/participant_edit.html', context)


def participant_delete(request, tender_id, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    tender = get_object_or_404(Tender, id=tender_id)
    participant.delete()
    url = '/tender/' + str(tender.id) + '/'
    return redirect(url)


def goods_add(request, tender_id, participant_id):
    tender = get_object_or_404(Tender, id=tender_id)
    participant = get_object_or_404(Participant, id=participant_id)
    products = Product.objects.all().order_by('name')
    context = {
        'tender': tender,
        'participant': participant,
        'products': products,
    }
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            url = '/tender/' + str(tender.id) + '/' + str(participant.id) + '/'
            return redirect(url)
    return render(request, 'tender/goods_add.html', context)


def goods_edit(request, tender_id, participant_id, goods_id):
    tender = get_object_or_404(Tender, id=tender_id)
    participant = get_object_or_404(Participant, id=participant_id)
    goods = get_object_or_404(Goods, id=goods_id)
    context = {
        'tender': tender,
        'participant': participant,
        'goods': goods,
    }
    if request.method == 'POST':
        form = GoodsForm(request.POST, instance=goods)
        if form.is_valid():
            form.save()
            url = '/tender/' + str(tender.id) + '/' + str(participant.id) + '/'
            return redirect(url)
    return render(request, 'tender/goods_edit.html', context)


def goods_delete(request, tender_id, participant_id, goods_id):
    participant = get_object_or_404(Participant, id=participant_id)
    tender = get_object_or_404(Tender, id=tender_id)
    goods = get_object_or_404(Goods, id=goods_id)
    goods.delete()
    url = '/tender/' + str(tender.id) + '/' + str(participant.id) + '/'
    return redirect(url)
