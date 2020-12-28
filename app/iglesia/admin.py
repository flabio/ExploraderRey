from django.contrib import admin
from app.iglesia.models import Iglesia
# Register your models here.
@admin.register(Iglesia)
class IglesiaAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre','direccion','telefono','correo')
    list_display_links = ('pk','nombre')
    list_editable = ('direccion','telefono','correo')
    search_fields = ('nombre','correo','telefono')
    list_filter   = ('created','modified','estado')
    fieldsets = (
        ('Iglesia', {
            'fields': (
                        ('nombre', 'direccion'),
                        ('telefono', 'correo','estado'),
                    ),
        }),
       
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)