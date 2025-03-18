from django.contrib.auth.models import User
from django.db import models


class Owner(User):

    TYPES = (
        (1, 'Persona Natural'),
        (2, 'Persona Jurídica'),
    )

    ID_TYPES = (
        (1, 'Cédula de ciudadanía'),
        (2, 'NIT'),
        (3, 'Pasaporte'),
    )

    type = models.IntegerField(verbose_name='Tipo de persona', choices=TYPES)
    identification_type = models.IntegerField(verbose_name='Tipo de identificación', choices=ID_TYPES)
    identification_number = models.CharField(verbose_name='Número de identificación', max_length=20, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'