from django.conf import settings
from django.db import models


class Infraction(models.Model):

    CATEGORIES = (
        ('A', 'A: Infracciones al conductor de un vehículo no automotor o de tracción animal'),
        ('B', 'B: Infracciones al conductor y/o propietario de un vehículo automotor'),
        ('C', 'C: Infracciones al conductor y/o propietario de un vehículo automotor'),
        ('D', 'D: Infracciones al conductor y/o propietario de un vehículo automotor'),
        ('E', 'E: Infracciones al conductor y/o propietario de un vehículo automotor'),
        ('FF', 'FF: Conducir en estado de embriaguez'),
        ('F', 'F: Infracciones al peatón'),
        ('G', 'G: Infracciones comparendos educativos'),
        ('H', 'H: Infracciones al conductor, pasajero o peatón'),
        ('I', 'I: Infracciones de sanciones pecuniarias de diferentes montos'),
        ('J', 'J: Otras infracciones de competencia de las autoridades de tránsito')
    )

    category = models.CharField(verbose_name='Categoría', max_length=2, choices=CATEGORIES)
    code = models.CharField(verbose_name='Código', max_length=4, unique=True)
    description = models.TextField(verbose_name='Descripción')
    fine = models.IntegerField(verbose_name='Multa en SMDLV')
    impound = models.BooleanField(verbose_name='Inmovilización', default=False)

    def get_value(self):
        return self.fine * settings.SMDLV

    def __str__(self):
        return f'{self.code} - {self.description}'

    class Meta:
        verbose_name = 'Infracción'
        verbose_name_plural = 'Infracciones'    


class Violation(models.Model):

    CREATORS = (
        (1, 'Agente de tránsito'),
        (2, 'Cámara de seguridad'),
    )

    infraction = models.ForeignKey('violations.Infraction', on_delete=models.CASCADE)
    created_by = models.IntegerField(verbose_name='Creado por', choices=CREATORS)
    created_at = models.DateTimeField(verbose_name='Fecha y hora de creación', auto_now_add=True)
    officer = models.ForeignKey('officers.Officer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.infraction.code} - {self.vehicle.license_plate}'

    class Meta:
        verbose_name = 'Comparendo'
        verbose_name_plural = 'Comparendos'
