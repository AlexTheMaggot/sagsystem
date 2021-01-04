import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenderForm, ProductForm, ProductCategoryForm, ProviderForm, ParticipantForm, GoodsForm, OrganizationForm
from .models import Tender, Product, Provider, ProductCategory, Participant, Goods, Price, SelectedPrice, Organization
from mainapp.models import Measure
from django_pandas.io import read_frame


def tender_list(request):
    if request.user.is_authenticated:
        tenders = Tender.objects.all().order_by('name')
        context = {
            'tenders': tenders,
        }
        return render(request, 'tender/tender_list.html', context)
    else:
        return redirect('/auth/')


def tender_cfo_true(request):
    if request.user.is_authenticated:
        tenders = Tender.objects.filter(cfo_confirm__exact=True)
        context = {
            'tenders': tenders,
        }
        return render(request, 'tender/tender_list.html', context)
    else:
        return redirect('/auth/')


def tender_cfo_false(request):
    if request.user.is_authenticated:
        tenders = Tender.objects.filter(cfo_confirm__exact=False)
        context = {
            'tenders': tenders,
        }
        return render(request, 'tender/tender_list.html', context)
    else:
        return redirect('/auth/')


def tender_cfo_null(request):
    if request.user.is_authenticated:
        tenders = Tender.objects.filter(cfo_confirm__exact=None)
        context = {
            'tenders': tenders,
        }
        return render(request, 'tender/tender_list.html', context)
    else:
        return redirect('/auth/')


def tender_detail(request, tender_id):
    if request.user.is_authenticated:
        tender = get_object_or_404(Tender, id=tender_id)
        participants = Participant.objects.all().filter(tender_id__exact=tender_id).order_by('provider__name')
        goods = Goods.objects.all().filter(tender_id__exact=tender_id).order_by('product__name')
        prices = Price.objects.filter(tender_id=tender_id)
        selected_prices = SelectedPrice.objects.filter(tender_id=tender_id).order_by('price__goods__product__name')

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
    else:
        return redirect('/auth/')


def tender_add(request):
    if request.user.is_authenticated:
        organizations = Organization.objects.all().order_by('name')
        context = {
            'organizations': organizations,
        }
        if request.method == 'POST':
            form = TenderForm(request.POST)
            if form.is_valid():
                form.save()
                url = '/tender/' + str(form.save().id) + '/'
                return redirect(url)
        return render(request, 'tender/tender_add.html', context)
    else:
        return redirect('/auth/')


def tender_delete(request, tender_id):
    if request.user.is_authenticated:
        provider = get_object_or_404(Tender, id=tender_id)
        provider.delete()
        return redirect('/tender/')
    else:
        return redirect('/auth/')


def tender_edit(request, tender_id):
    if request.user.is_authenticated:
        tender = get_object_or_404(Tender, id=tender_id)
        organizations = Organization.objects.all().order_by('name')
        if request.method == 'POST':
            form = TenderForm(request.POST, instance=tender)
            if form.is_valid():
                form.save()
                url = '/tender/' + str(form.save().id) + '/'
                return redirect(url)

        context = {
            'tender': tender,
            'organizations': organizations,
        }
        return render(request, 'tender/tender_edit.html', context)
    else:
        return redirect('/auth/')


def tender_cpo_confirm(request, tender_id):
    if request.user.is_authenticated:
        tender = get_object_or_404(Tender, id=tender_id)
        url = '/tender/' + str(tender.id) + '/'
        if request.user.id == 8:
            tender.cpo_confirm = True
            time = datetime.datetime.now()
            tender.cpo_confirm_date = time
            tender.save()
        return redirect(url)
    else:
        return redirect('/auth/')


def tender_cfo_confirm(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)
    url = '/tender/' + str(tender.id) + '/'
    if request.user.id == 13:
        tender.cfo_confirm = True
        tender.cfo_confirm_date = datetime.datetime.now()
        tender.save()
    return redirect(url)


def tender_cpo_reject(request, tender_id):
    if request.user.is_authenticated:
        tender = get_object_or_404(Tender, id=tender_id)
        url = '/tender/' + str(tender.id) + '/'
        if request.method == 'POST' and request.user.id == 8:
            tender.cpo_confirm = False
            tender.cpo_comment = request.POST['text']
            tender.cpo_confirm_date = datetime.datetime.now()
            tender.save()
        return redirect(url)
    else:
        return redirect('/auth/')


def tender_cfo_reject(request, tender_id):
    if request.user.is_authenticated:
        tender = get_object_or_404(Tender, id=tender_id)
        url = '/tender/' + str(tender.id) + '/'
        if request.method == 'POST' and request.user.id == 13:
            tender.cfo_confirm = False
            tender.cfo_comment = request.POST['text']
            tender.cfo_confirm_date = datetime.datetime.now()
            tender.save()
        return redirect(url)
    else:
        return redirect('/auth/')


def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('name')
        categories = ProductCategory.objects.all().order_by('name')
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'tender/product_list.html', context)
    else:
        return redirect('/auth/')


def product_add(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('/auth/')


def product_delete(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect('/tender/products')
    else:
        return redirect('/auth/')


def product_edit(request, id):
    if request.user.is_authenticated:
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
    else:
        return redirect('/auth/')


def product_by_category(request, id):
    if request.user.is_authenticated:
        products = Product.objects.filter(category_id__exact=id).order_by('name')
        categories = ProductCategory.objects.all().order_by('name')
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'tender/product_list.html', context)
    else:
        return redirect('/auth/')


def product_category_list(request):
    if request.user.is_authenticated:
        product_categories = ProductCategory.objects.all().order_by('name')
        context = {
            'product_categories': product_categories,
        }
        return render(request, 'tender/product_category_list.html', context)
    else:
        return redirect('/auth/')


def product_category_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/tender/product-category/')
        return render(request, 'tender/product_category_add.html')
    else:
        return redirect('/auth/')


def product_category_delete(request, id):
    if request.user.is_authenticated:
        product_category = get_object_or_404(ProductCategory, id=id)
        product_category.delete()
        return redirect('/tender/product-category/')
    else:
        return redirect('/auth/')


def product_category_edit(request, id):
    if request.user.is_authenticated:
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
    else:
        return redirect('/auth/')


def provider_list(request):
    if request.user.is_authenticated:
        providers = Provider.objects.all().order_by('name')
        context = {
            'providers': providers,
        }
        return render(request, 'tender/provider_list.html', context)
    else:
        return redirect('/auth/')


def provider_detail(request, id):
    if request.user.is_authenticated:
        provider = get_object_or_404(Provider, id=id)

        context = {
            'provider': provider,
        }
        return render(request, 'tender/provider_detail.html', context)
    else:
        return redirect('/auth/')


def provider_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProviderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/tender/providers/')
        return render(request, 'tender/provider_add.html')
    else:
        return redirect('/auth/')


def provider_delete(request, id):
    if request.user.is_authenticated:
        provider = get_object_or_404(Provider, id=id)
        provider.delete()
        return redirect('/tender/providers/')
    else:
        return redirect('/auth/')


def provider_edit(request, id):
    if request.user.is_authenticated:
        provider = get_object_or_404(Provider, id=id)

        if request.method == 'POST':
            form = ProviderForm(request.POST, instance=provider)
            if form.is_valid():
                form.save()
                return redirect('/tender/providers/')

        context = {
            'provider': provider,
        }
        return render(request, 'tender/provider_edit.html', context)
    else:
        return redirect('/auth/')


def participant_add(request, tender_id):
    if request.user.is_authenticated:
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
                add_another = '/tender/' + str(tender.id) + '/participant_add/'
                if 'save' in request.POST:
                    return redirect(url)
                elif 'add_another' in request.POST:
                    return redirect(add_another)
        return render(request, 'tender/participant_add.html', context)
    else:
        return redirect('/auth/')


def participant_delete(request, tender_id, participant_id):
    if request.user.is_authenticated:
        participant = get_object_or_404(Participant, id=participant_id)
        tender = get_object_or_404(Tender, id=tender_id)
        participant.delete()
        url = '/tender/' + str(tender.id) + '/'
        return redirect(url)
    else:
        return redirect('/auth/')


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
            add_another = '/tender/' + str(tender.id) + '/goods_add/'
            if 'save' in request.POST:
                return redirect(url)
            elif 'add_another' in request.POST:
                return redirect(add_another)
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
    prices = Price.objects.filter(tender_id=tender_id).order_by('participant')
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
        for p in prices:
            winner = 'winner_' + str(p.goods.product.id)
            winner_price = 'winner_' + str(p.id)
            quantity = 'quantity_' + str(p.id)
            if winner in request.POST:
                if winner_price in request.POST[winner]:
                    sum = float(p.price) * float(request.POST[quantity])
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
    if request.method == 'POST':
        for sw in selected_winners:
            sw.delete()
        for p in prices:
            winner = 'winner_' + str(p.goods.product.id)
            winner_price = 'winner_' + str(p.id)
            quantity = 'quantity_' + str(p.id)
            if winner in request.POST:
                if winner_price in request.POST[winner]:
                    sum = float(p.price) * float(request.POST[quantity])
                    add = SelectedPrice(tender_id=tender_id, price_id=p.id, quantity=request.POST[quantity], sum=sum)
                    add.save()
        return redirect('/tender/' + str(tender_id) + '/')
    return render(request, 'tender/select_winners_edit.html', context)


def organization_list(request):
    organizations = Organization.objects.all().order_by('name')
    context = {
        'organizations': organizations,
    }
    return render(request, 'tender/organization_list.html', context)


def organization_add(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tender/organizations/')
    return render(request, 'tender/organization_add.html')


def organization_delete(request, id):
    organization = get_object_or_404(Organization, id=id)
    organization.delete()
    return redirect('/tender/organizations/')


def organization_edit(request, id):
    organization = get_object_or_404(Organization, id=id)

    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('/tender/organizations/')

    context = {
        'organization': organization,
    }
    return render(request, 'tender/organization_edit.html', context)
