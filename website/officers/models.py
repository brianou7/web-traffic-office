from django.db import models


class Officer(models.Model):
    
    TYPES = (
        (1, 'Agente'),
        (2, 'Supervisor'),
    )

    type = models.IntegerField(verbose_name='Tipo de funcionario', choices=TYPES)
    first_name = models.CharField(verbose_name='Nombre', max_length=30)
    last_name = models.CharField(verbose_name='Apellido', max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Oficial'
        verbose_name_plural = 'Oficiales de tránsito'
