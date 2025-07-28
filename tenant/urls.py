from django.urls import path
from .views import (
    MaintanceView,
    MessageView,
    PaymentView,
    create_tenant,
)
urlpatterns = [
    path('maintance/', MaintanceView.as_view(), name='maintance'),
    path('message/', MessageView.as_view(), name='message'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('create/', create_tenant, name='create-tenant'), 
]