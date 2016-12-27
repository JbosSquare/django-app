from django.db import models
from django.utils import timezone

# Create your models here.
class ClienteForm(models.Model):
    nomeCliente = models.TextField()
    cpf = models.CharField(max_length=11)
    created_date = models.DateTimeField(default = timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.nomeCliente