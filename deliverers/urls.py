from django.urls import path

from deliverers.views import DelivererCreateView, DelivererListView

urlpatterns = [
    path('edit', DelivererCreateView.as_view(), name='edit-deliverer'),
    path('list', DelivererListView.as_view(), name='list-deliverers')
]
