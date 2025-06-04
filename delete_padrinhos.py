import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.contrib.auth import get_user_model
from apadrinhamento.models import Padrinho

User = get_user_model()

# Deletar todos os usuários
deleted_users, _ = User.objects.all().delete()
print(f'{deleted_users} usuário(s) foram deletados.')

# Deletar todos os padrinhos
deleted_padrinhos, _ = Padrinho.objects.all().delete()
print(f'{deleted_padrinhos} padrinho(s) foram deletados.')
