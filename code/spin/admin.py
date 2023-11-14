from django.contrib import admin

# Register your models here.

from spin.models import Spins


class SpinAdmin(admin.ModelAdmin):
    list_display = ('created', 'strip1', 'strip2', 'strip3',
                    'strip4', 'strip5', 'strip6', 'win')


admin.site.register(Spins, SpinAdmin)
