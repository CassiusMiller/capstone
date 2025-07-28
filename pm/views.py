from django.views.generic import TemplateView

# Create your views here.
class portfolioView(TemplateView):
    template_name = 'pm/portfolio.html'
class tenantview(TemplateView):
    template_name = 'pm/tenant.html'
class messagesView(TemplateView):
    template_name = 'pm/messages.html'
class maintancereqView(TemplateView):
    template_name = 'pm/maintenancereq.html'
class contractsView(TemplateView):
    template_name = 'pm/contracts.html'
class financialsView(TemplateView):
    template_name = 'pm/financials.html'
class taxView(TemplateView):
    template_name = 'pm/1099.html'