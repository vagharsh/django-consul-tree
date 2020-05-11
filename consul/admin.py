from django.contrib import admin
from django.contrib.admin import ModelAdmin
from consul.models import Consul


class ConsulAdmin(ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'url')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Consul, ConsulAdmin)
