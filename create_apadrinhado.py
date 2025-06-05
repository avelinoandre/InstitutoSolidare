import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apadrinhamento.models import Apadrinhado

dados = {
    "nome": "teste",
    "data_nascimento": date(2010, 1, 1),
    "genero": "Masculino",
    "info": "Informações adicionais sobre o apadrinhado.",
    "endereco": "Rua dos Testes, 123",
    "area_escolar": 1,
    "profissao_desejada": 2,
    "hobby": 3,
    "inspiracoes": 4,
    "valores": 5,
}

apadrinhado = Apadrinhado.objects.create(**dados)

print(f'Apadrinhado criado com id: {apadrinhado.id} e nome: {apadrinhado.nome}')
