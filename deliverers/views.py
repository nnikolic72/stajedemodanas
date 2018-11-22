# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView

from deliverers.forms import DelivererForm
from deliverers.models import Deliverer, DeliveryItem

from stajedemodanas.views import BaseView


class DelivererCreateView(CreateView):
    model = Deliverer
    template_name = 'deliverer_form.html'
    form_class = DelivererForm


class DelivererListView(BaseView):
    def get(self, request):
        deliverers_and_items = dict()
        deliverers = Deliverer.objects.all()
        for deliverer in deliverers:
            items = DeliveryItem.objects.filter(deliverer=deliverer)
            deliverers_and_items[deliverer.id] = dict()
            deliverers_and_items[deliverer.id]['deliverer'] = deliverer
            deliverers_and_items[deliverer.id]['delivereritems'] = items
        self.context['deliverers'] = deliverers_and_items

        return render(request, template_name='deliverers-list.html', context=self.context)
