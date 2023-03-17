from django.contrib import admin


from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district']
    readonly_fields = ['created_at',]
    list_display = ('town_district', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    pass


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']
    pass


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
