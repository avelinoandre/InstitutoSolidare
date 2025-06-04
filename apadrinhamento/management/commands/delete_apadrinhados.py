from django.core.management.base import BaseCommand
from apadrinhamento.models import Apadrinhado

class Command(BaseCommand):
    help = 'Apaga todos os registros da tabela Apadrinhado'

    def handle(self, *args, **kwargs):
        total = Apadrinhado.objects.count()
        Apadrinhado.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"{total} registros apagados da tabela Apadrinhado."))
