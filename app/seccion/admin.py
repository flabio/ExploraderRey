from django.contrib import admin
#models
from app.seccion.models import Seccion
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('pk','user','seccion')
    list_editable = ('user','seccion')
    search_fields = ('seccion','user')
    list_filter   = ('created','modified','estado')
    fieldsets = (
        ('Seccion', {
            'fields': (
                        ('seccion', 'user','estado'),
                    ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)