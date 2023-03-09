from django.contrib import admin


from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_destrict']
    pass

admin.site.register(Flat, FlatAdmin)
