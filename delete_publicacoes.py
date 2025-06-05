import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apadrinhamento.models import Publicacao  

deleted, _ = Publicacao.objects.all().delete()

print(f'{deleted} publicação(ões) foram deletadas.')
