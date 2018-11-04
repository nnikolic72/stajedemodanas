# Create your views here.
from django.views.generic import CreateView

from deliverers.forms import DelivererForm
from deliverers.models import Deliverer


class DelivererCreateView(CreateView):
    model = Deliverer
    template_name = 'deliverer_form.html'
    form_class = DelivererForm
