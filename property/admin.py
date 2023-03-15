from django.contrib import admin


from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district']
    readonly_fields = ['created_at',]
    list_display = ('town_district', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ['new_building']
    pass

admin.site.register(Flat, FlatAdmin)
