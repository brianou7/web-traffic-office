from django.db import models


class Vehicle(models.Model):

    TYPES = (
        (1, 'Automóvil'),
        (2, 'Motocicleta'),
        (3, 'Vehículo pesado'),
    )

    type = models.IntegerField(verbose_name='Tipo de vehículo', choices=TYPES)
    license_plate = models.CharField(verbose_name='Placa', max_length=10)
    brand = models.CharField(verbose_name='Marca', max_length=255)
    model = models.CharField(verbose_name='Modelo', max_length=255)
    year = models.IntegerField(verbose_name='Año')

    since = models.DateField(verbose_name='Fecha de registro')
    owner = models.ForeignKey('owners.Owner', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
