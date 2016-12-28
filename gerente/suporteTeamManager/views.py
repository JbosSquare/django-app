from django.shortcuts import render
from django.utils import timezone
from .models import ClienteForm

# Create your views here.
def clientes_list(request):
    clientes = ClienteForm.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request,'suporteTeamManager/clientes_list.html',{'clientes' : clientes})