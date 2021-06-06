from django.shortcuts import render, redirect
from .forms import AddLinkForm
from .models import Link
from django.views.generic import DetailView
from django.urls import reverse_lazy


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


class LinkDeleteView(DetailView):
    model = Link
    template_name = 'Link/confirm_delete.html'
    success_url = reverse_lazy('home_view')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home_view')