from django.contrib import admin
from .models import RecordHourExtra


##admin.site.register(RecordHourExtra) = 'My Site Admin'

@admin.register(RecordHourExtra)
class RecordHourExtraAdmin(admin.ModelAdmin):
    list_display = ("employee", "reason")
    fieldsets = (
        (None, {
            'fields': ('employee',)
        }),
        (None, {
            'fields': ('reason',)
        }),     
    ) 

