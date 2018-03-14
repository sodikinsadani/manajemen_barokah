from django.contrib import admin
from training.models import Materi

class MateriAdmin(admin.ModelAdmin):
    list_display = ('judul_materi','jenjang',)

admin.site.register(Materi,MateriAdmin)
