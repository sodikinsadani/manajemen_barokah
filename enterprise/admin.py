from django.contrib import admin
from enterprise.models import Report, ParameterGlobal, Trainer

class ReportAdmin(admin.ModelAdmin):
    list_display = ('nama_laporan','script','app',)

admin.site.register(Report,ReportAdmin)

class GlobalAdmin(admin.ModelAdmin):
    list_display = ('id','nama_parameter','nilai_parameter',)

admin.site.register(ParameterGlobal,GlobalAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('nama_trainer',)

admin.site.register(Trainer,TrainerAdmin)
