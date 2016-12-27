from django.shortcuts import render

# Create your views here.
def clientes_list(request):
    return render(request,'suporteTeamManager/clientes_list.html',{})