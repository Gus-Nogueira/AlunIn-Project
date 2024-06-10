from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def list(request):
    vagas = [
        {'id': 1, 'title': 'Vaga 1'},
        {'id': 2, 'title': 'Vaga 2'}
    ]
    return render(request, 'list.html', {'vagas': vagas})

def detail(request, vaga_id):
    vaga = {'id': vaga_id, 'title': f'Vaga {vaga_id}', 'description': 'Descrição', 'requirements': 'Requisitos', 'location': 'Localização', 'job_type': 'Estágio'}
    return render(request, 'detail.html', {'vaga': vaga})

def apply(request, vaga_id):
    vaga = {'id': vaga_id, 'title': f'Vaga {vaga_id}'}
    if request.method == 'POST':
        return HttpResponse("Aplicação enviada com sucesso!")
    return render(request, 'apply.html', {'vaga': vaga})
