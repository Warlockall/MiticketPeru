from django.db import models


class Cliente(models.Model):
    NombresApellidos  = models.CharField(max_length=100)
    TipoDoc           = models.CharField(max_length=10)
    NumeroDoc         = models.CharField(max_length=20)
    Nacionalidad      = models.CharField(max_length=20)
    FechaNac          = models.DateField()
    Telefono          = models.CharField(max_length=15, blank=True, null=True)
    DocScaneado       = models.ImageField(upload_to='Media',blank=True, null=True)
    Observacion       = models.TextField(blank=True, null=True)

    def __unicode__(self):
    	return self.NombresApellidos

class Lugares(models.Model):
    Origen    = models.CharField(max_length=30)
    Destino   = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30,blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Lugares'

    def __unicode__(self):
    	return "%s - %s" % (self.Origen, self.Destino)

Choice_Categoria=(('Privado','Privado'), ('Grupal','Grupal'))
class Transporte(models.Model):
    TipoTransporte   = models.CharField(max_length=20) #
    NombreTransporte = models.CharField(max_length=20)
    PrivadoGrupal       = models.CharField(choices=Choice_Categoria, max_length=10) #false=grupal, true=privado

    def __unicode__(self):
    	return "%s - %s - %s" % (self.TipoTransporte, self.NombreTransporte, self.PrivadoGrupal)

class Tour(models.Model):
    IdTransporte  = models.ForeignKey(Transporte)
    IdLugar       = models.ForeignKey(Lugares)
    Tarifa        = models.CharField(max_length=20, blank=True, null=True)
    Precio        = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    FechaCreacion = models.DateField(auto_now_add=True)

    def __unicode__(self):
    	return "%s - %s - %s- %s" % (self.id, self.IdTransporte, self.IdLugar, self.Tarifa)

class Paquete(models.Model):
    IdTour      = models.ManyToManyField(Tour)
    FechaIda    = models.DateField()
    FechaVuelta = models.DateField()

    def __unicode__(self):
        return "%s - %s - %s" % (self.id, self.FechaIda, self.FechaVuelta)

class Reserva(models.Model):
    IdCliente         = models.ManyToManyField(Cliente)
    IdPaquete         = models.ForeignKey(Paquete)
    LugarEntrega      = models.CharField(max_length=100)
    Comprado          = models.BooleanField(default=False)
    Email             = models.EmailField(blank=True, null=True)
    FechaReserva      = models.DateField(auto_now_add=True)

    def __unicode__(self):
    	return "%s - %s" % (self.IdCliente , self.LugarEntrega)
