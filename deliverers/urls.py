from django.urls import path

from deliverers.views import DelivererCreateView

urlpatterns = [
    path('edit', DelivererCreateView.as_view(), name='edit-deliverer')
]
