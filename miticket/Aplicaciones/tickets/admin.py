from django.contrib import admin
from .models import Cliente, Lugares, Transporte, Tour, Paquete, Reserva


# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['NumeroDoc']
    ordering = ['NumeroDoc']
    search_fields = ('NumeroDoc',)

class LugaresAdmin(admin.ModelAdmin):
    list_display = ['Origen']
    ordering = ['Origen']
    search_fields = ('Origen',)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Lugares,LugaresAdmin)
admin.site.register(Transporte)
admin.site.register(Tour)
admin.site.register(Paquete)
admin.site.register(Reserva)
