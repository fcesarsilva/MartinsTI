from django.shortcuts import render

def home(request):
        context = {'texto': 'Martins TI - Excelencia em Sistemas Web!!!'}
        return render(request, 'index.html', context)
# Create your views here.
