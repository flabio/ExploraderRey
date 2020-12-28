from django.contrib import admin
from app.destacamento.models import Destacamento
# Register your models here.
@admin.register(Destacamento)
class DestacamentoAdmin(admin.ModelAdmin):
    list_display = ('pk','iglesia','seccion','nombre','imagen','distrito','numero')
    list_display_links = ('pk','nombre')
    list_editable = ('imagen','distrito','numero')
    search_fields = ('nombre','distrito','numero')
    list_filter   = ('created','modified','estado')
    fieldsets = (
        ('Destacamento', {
            'fields': (
                        ('nombre', 'imagen'),
                        ('distrito', 'numero','estado'),
                    ),
        }),
        ('Otro', {
            'fields': (('iglesia', 'seccion'),),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)