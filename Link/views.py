from django.shortcuts import render
from .forms import AddLinkForm
from .models import Link


# Create your views here.
def home_view(request):
    number_discount = 0
    error = None
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = 'Oops , could not get the name or price'
        except:
            error = 'Oops, something went wrong'

    form = AddLinkForm()

    qs = Link.objects.all()
    items_number = qs.count()

    if items_number > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            number_discount = len(discount_list)

    context = {
        'qs': qs,
        'items_number': items_number,
        'number_discounted': number_discount,
        'form': form,
        'error': error
    }

    return render(request, 'Link/main.html', context)
