# InternalImports
from .models import Customer
from .forms import CustomerForm
from mainapp.views import check_access, group_list
# End InternalImports

# DjangoImports
from django.shortcuts import render, redirect, get_object_or_404, reverse
# End DjangoImports

# ExternalImports
import openpyxl
from openpyxl.styles import Font
# End ExternalImports


# CustomerViews
def customer_list(request):
    if check_access(request.user.groups.all(), 4) or check_access(request.user.groups.all(), 5):
        customers = Customer.objects.all()
        groups = group_list(request.user.groups.all())
        context = {
            'customers': customers,
            'groups': groups,
        }
        template = 'customers/customer_list.html'
        return render(request, template, context)
    else:
        return redirect('/')


def customer_detail(request, customer_id):
    if check_access(request.user.groups.all(), 4) or check_access(request.user.groups.all(), 5):
        customer = get_object_or_404(Customer, id=customer_id)
        groups = group_list(request.user.groups.all())
        context = {
            'customer': customer,
            'groups': groups,
        }
        template = 'customers/customer_detail.html'
        return render(request, template, context)
    else:
        return redirect('/')


def customer_add(request):
    if check_access(request.user.groups.all(), 4) or check_access(request.user.groups.all(), 5):
        if request.method == 'GET':
            groups = group_list(request.user.groups.all())
            context = {
                'groups': groups,
            }
            template = 'customers/customer_add.html'
            return render(request, template, context)
        elif request.method == 'POST':
            new_customer = CustomerForm(request.POST)
            if new_customer.is_valid():
                new_customer.save()
                url = '/customers/' + str(new_customer.save().id) + '/'
                return redirect(url)
    else:
        return redirect('/')


def customer_edit(request, customer_id):
    if check_access(request.user.groups.all(), 4) or check_access(request.user.groups.all(), 5):
        customer = get_object_or_404(Customer, id=customer_id)
        if request.method == 'GET':
            groups = group_list(request.user.groups.all())
            context = {
                'customer': customer,
                'groups': groups,
            }
            template = 'customers/customer_edit.html'
            return render(request, template, context)
        elif request.method == 'POST':
            edited_customer = CustomerForm(request.POST, instance=customer)
            if edited_customer.is_valid():
                edited_customer.save()
                url = '/customers/' + str(edited_customer.save().id) + '/'
                return redirect(url)
    else:
        return redirect('/')


def customer_delete(request, customer_id):
    if check_access(request.user.groups.all(), 4):
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return redirect('customers:customer_list')
    else:
        return redirect('/')


def customer_delete_bulk(request):
    if check_access(request.user.groups.all(), 4):
        customers = Customer.objects.all()
        customers.delete()
        return redirect('customers:customer_list')
    else:
        return redirect('/')


def customer_add_by_xlsx(request):
    if check_access(request.user.groups.all(), 4) or check_access(request.user.groups.all(), 5):
        if request.method == 'GET':
            groups = group_list(request.user.groups.all())
            template = 'customers/customer_add_by_xlsx.html'
            context = {
                'groups': groups,
            }
            return render(request, template, context)
        elif request.method == 'POST':
            file = request.FILES['table']
            wt = openpyxl.load_workbook(file)
            ws = wt.active
            title = True
            adding_data = {
                'name': None,
                'phone': None,
                'date_of_birth': None,
                'sex': None,
                'address': None,
                'telegram': None,
                'facebook': None,
                'instagram': None,
                'comment': None,
            }
            data = []
            for row in ws:
                if title is True:
                    title = False
                else:
                    n = 0
                    for cell in row:
                        if n == 0:
                            adding_data['name'] = cell.value
                        elif n == 1:
                            adding_data['phone'] = cell.value
                        elif n == 2:
                            adding_data['date_of_birth'] = cell.value
                        elif n == 3:
                            adding_data['sex'] = cell.value
                        elif n == 4:
                            adding_data['address'] = cell.value
                        elif n == 5:
                            adding_data['telegram'] = cell.value
                        elif n == 6:
                            adding_data['facebook'] = cell.value
                        elif n == 7:
                            adding_data['instagram'] = cell.value
                        elif n == 8:
                            adding_data['comment'] = cell.value
                        n += 1
                    data_item = Customer(name=adding_data['name'], phone=adding_data['phone'],
                                         date_of_birth=adding_data['date_of_birth'], sex=adding_data['sex'],
                                         address=adding_data['address'], telegram=adding_data['telegram'],
                                         facebook=adding_data['facebook'], instagram=adding_data['instagram'],
                                         comment=adding_data['comment'])
                    data.append(data_item)
            Customer.objects.bulk_create(data)
            return redirect('customers:customer_list')
    else:
        return redirect('/')


def customer_export(request):
    if check_access(request.user.groups.all(), 4):
        customers = Customer.objects.all()
        table = openpyxl.Workbook()
        ws = table.active
        ws.append(['ФИО', 'Номер Телефона', 'Дата Рождения', 'Пол', 'Адрес', 'Telegram', 'Facebook', 'Instagram',
                   'Comment', ])
        for row in ws:
            for cell in row:
                cell.font = Font(bold=True)
        for customer in customers:
            add_list = [str(customer.name), str(customer.phone), str(customer.date_of_birth), str(customer.sex),
                        str(customer.address), str(customer.telegram), str(customer.facebook), str(customer.instagram),
                        str(customer.comment), ]
            print(add_list)
            for item in range(len(add_list)):
                if add_list[item] == 'None':
                    add_list[item] = None
            print(add_list)
            ws.append(add_list)

        dist = 'mainapp/static/temp/export.xlsx'

        table.save(filename=dist)

        return redirect('customers:customer_export_ready')
    else:
        return redirect('/')


def customer_export_ready(request):
    if check_access(request.user.groups.all(), 4):
        template = 'customers/customer_export_ready.html'
        return render(request, template)
    else:
        return redirect('/')
# End CustomerViews
