from django.contrib import admin
from personalia.models import Pangkal, Individu, Member

class PangkalAdmin(admin.ModelAdmin):
    list_display = ('id_pk','nama','rt',)

admin.site.register(Pangkal,PangkalAdmin)

class IndividuAdmin(admin.ModelAdmin):
    list_display = ('nama','tgl_lahir','tmpt_lahir','jk','alamat',
        'alamat_desa','alamat_kec','alamat_kabkot','alamat_prov','lulusan','hp',)
    search_fields = ['nama']
    list_display_links = ['nama']

admin.site.register(Individu,IndividuAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('individu','jenjang','tgl_daftar','status_aktif',
        'segmentasi','pangkal','warga_media','keterangan','tgl_input')
    raw_id_fields = ("individu",)

admin.site.register(Member,MemberAdmin)



