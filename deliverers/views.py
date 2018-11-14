# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView

from deliverers.forms import DelivererForm
from deliverers.models import Deliverer

from stajedemodanas.views import BaseView


class DelivererCreateView(CreateView):
    model = Deliverer
    template_name = 'deliverer_form.html'
    form_class = DelivererForm


class DelivererListView(BaseView):
    def get(self, request):
        self.context['deliverers'] = Deliverer.objects.all()
        return render(request, template_name='deliverers-list.html', context=self.context)
