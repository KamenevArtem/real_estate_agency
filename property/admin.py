from django.contrib import admin


from .models import Flat, Complaint, Owner


class AdminInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'id']
    readonly_fields = ['created_at',]
    list_display = ('town_district', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [AdminInline]
    pass


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']
    pass


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    inlines = [AdminInline]
    exclude = ['flats']
    pass






admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
