from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

@login_required
def create_tenant(request):
    if not request.user.is_property_manager:
        raise PermissionDenied("Only property managers can create tenants.")
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.is_tenant = True
            tenant.save()
            return redirect('tenant-dashboard')  # change as needed
    else:
        form = UserCreationForm()
    
    return render(request, 'tenant/create_tenant.html', {'form': form})
    

# Create your views here.
class MaintanceView(TemplateView):
    template_name = 'tenant/maintance.html'
class MessageView(TemplateView):
    template_name = 'tenant/message.html'
class PaymentView(TemplateView):
    template_name = 'tenant/payment.html'