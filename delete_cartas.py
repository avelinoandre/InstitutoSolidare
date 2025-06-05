import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apadrinhamento.models import Carta

deleted, _ = Carta.objects.all().delete()

print(f'{deleted} carta(s) foram deletadas.')
