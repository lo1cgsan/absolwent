from django.contrib import admin
from wiadomosci import models

# admin.site.register(models.Wiadomosc)
from django.forms import Textarea
from django.db.models.fields import TextField


@admin.register(models.Wiadomosc)
class WiadomoscAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    list_display = ('wiadomosc_skrot', 'autor', 'data_d')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()

