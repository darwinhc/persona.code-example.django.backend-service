from django.db import models


class Persona(models.Model):

    class Meta:
        unique_together = (('tipo_documento', 'documento'))


    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.IntegerField()
    # 0: Registro civil
    # 1: Tarjeta de identidad
    # 2: Cedula de ciudadanía
    # 3: Contraseña
    # 4: Pasaporte
    documento = models.CharField(max_length=255)
    hobbie = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Persona {self.nombre}-{self.documento}" 