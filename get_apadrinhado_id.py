import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from django.contrib.auth import get_user_model
from apadrinhamento.models import Padrinho, Apadrinhado

User = get_user_model()

username = "teste"

try:
    user = User.objects.get(username=username)
    padrinho = user.padrinho
    afilhado = Apadrinhado.objects.filter(padrinho=padrinho).order_by('id').first()
    if afilhado:
        print(afilhado.id)
    else:
        print("")
except (User.DoesNotExist, Padrinho.DoesNotExist):
    print("")
