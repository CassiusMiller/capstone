from django.urls import path
from .views import (
    portfolioView,
    tenantview,
    messagesView,
    maintancereqView,
    contractsView,
    financialsView,
    taxView,
)

urlpatterns = [
    path('portfolio/', portfolioView.as_view(), name='portfolio'),
    path('tenant/', tenantview.as_view(), name='tenant'),
    path('messages/', messagesView.as_view(), name='messages'),
    path('maintenancereq/', maintancereqView.as_view(), name='maintenancereq'),
    path('contracts/', contractsView.as_view(), name='contracts'),
    path('financials/', financialsView.as_view(), name='financials'),
    path('tax/', taxView.as_view(), name='tax'),
]