from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenderForm, ProductForm, ProductCategoryForm, ProviderForm, ParticipantForm, GoodsForm
from .models import Tender, Product, Provider, ProductCategory, Participant, Goods, Price, SelectedPrice
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
    prices = Price.objects.filter(tender_id=tender_id)
    selected_prices = SelectedPrice.objects.filter(tender_id=tender_id)
    context = {
        'tender': tender,
        'participants': participants,
        'goods': goods,
        'selected_prices': selected_prices,
    }
    if prices:
        fieldnames = ['goods__product__name', 'participant__provider__name', 'price']
        rows = ['goods__product__name']
        cols = ['participant__provider__name']
        values = 'price'
        df = prices.to_pivot_table(rows=rows, cols=cols, values=values, fieldnames=fieldnames, verbose=True)
        table = df.to_html(classes=['table', 'table-striped'])
        context['table'] = table
    return render(request, 'tender/tender_detail.html', context)


def tender_add(request):
    if request.method == 'POST':
        form = TenderForm(request.POST)
        if form.is_valid():
            form.save()
            url = '/tender/' + str(form.save().id) + '/'
            return redirect(url)
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
    goods = Goods.objects.filter(tender_id=tender_id)
    context = {
        'tender': tender,
        'providers': providers,
    }
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            for g in goods:
                price = Price.objects.create(tender_id=g.tender_id, goods_id=g.id, participant_id=form.save().id,
                                             price=0)
            url = '/tender/' + str(tender.id) + '/'
            return redirect(url)
    return render(request, 'tender/participant_add.html', context)


def participant_delete(request, tender_id, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    tender = get_object_or_404(Tender, id=tender_id)
    participant.delete()
    url = '/tender/' + str(tender.id) + '/'
    return redirect(url)


def goods_add(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    products = Product.objects.all().order_by('name')
    participants = Participant.objects.filter(tender_id=tender_id)
    categories = ProductCategory.objects.all()
    context = {
        'tender': tender,
        'products': products,
        'categories': categories,
    }
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            for p in participants:
                price = Price.objects.create(tender_id=p.tender_id, participant_id=p.id, goods_id=form.save().id,
                                             price=0)
            url = '/tender/' + str(tender.id) + '/'
            return redirect(url)
    return render(request, 'tender/goods_add.html', context)


def goods_delete(request, tender_id, goods_id):
    tender = get_object_or_404(Tender, id=tender_id)
    goods = get_object_or_404(Goods, id=goods_id)
    goods.delete()
    url = '/tender/' + str(tender.id) + '/'
    return redirect(url)


def prices_edit(request, tender_id):
    tender = Tender.objects.get(id=tender_id)
    prices = Price.objects.filter(tender_id=tender_id).order_by('goods')
    context = {
        'prices': prices,
        'tender': tender,
    }
    if request.method == 'POST':
        for p in prices:
            form = request.POST[str(p.id)]
            change_price = Price.objects.get(id=p.id)
            change_price.price = form
            change_price.save()
        url = '/tender/' + str(tender_id) + '/'
        return redirect(url)
    return render(request, 'tender/prices_edit.html', context)


def select_winners(request, tender_id):
    prices = Price.objects.filter(tender_id=tender_id).order_by('goods')
    tender = Tender.objects.get(id=tender_id)
    context = {
        'prices': prices,
        'tender': tender,
    }
    if request.method == 'POST':

        print(request.POST)
        for p in prices:
            winner = 'winner_' + str(p.goods.product.id)
            winner_price = 'winner_' + str(p.id)
            quantity = 'quantity_' + str(p.id)
            if winner in request.POST:
                if winner_price in request.POST[winner]:
                    sum = int(p.price) * int(request.POST[quantity])
                    add = SelectedPrice(tender_id=tender_id, price_id=p.id, quantity=request.POST[quantity], sum=sum)
                    add.save()
        return redirect('/tender/' + str(tender_id) + '/')

    return render(request, 'tender/select_winners.html', context)


def select_winners_delete(request, tender_id):
    selected_winners = SelectedPrice.objects.filter(tender_id=tender_id)
    url = '/tender/' + str(tender_id) + '/'
    for sw in selected_winners:
        sw.delete()
    return redirect(url)


def select_winners_edit(request, tender_id):
    prices = Price.objects.filter(tender_id=tender_id).order_by('goods')
    tender = Tender.objects.get(id=tender_id)
    selected_winners = SelectedPrice.objects.filter(tender_id=tender_id)
    context = {
        'prices': prices,
        'tender': tender,
        'selected_winners': selected_winners,
    }
    return render(request, 'tender/select_winners_edit.html', context)
