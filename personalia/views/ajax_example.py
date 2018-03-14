from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views import View
from personalia.models import Member

class getDataJson(View):
    def post(self, request):
        if self.request.is_ajax():
            id_member = request.POST['id_member']
            member = Member.objects.get(pk=id_member)
            tgl_lahir = member.individu.tgl_lahir
            data = {
                'id_member' : member.id_member,
                'nama' : member.individu.nama,
                'tmpt_lahir' : member.individu.tmpt_lahir,
                'tgl_lahir' : member.individu.tgl_lahir,
                'jk' : member.individu.jk,
                'alamat' : member.individu.alamat,
                'alamat_desa' : member.individu.alamat_desa,
                'alamat_kec' : member.individu.alamat_kec,
                'alamat_kabkot' : member.individu.alamat_kabkot,
                'alamat_prov' : member.individu.alamat_prov,
                'lulusan' : member.individu.lulusan,
                'hp' : member.individu.hp,
                'jenjang' : member.jenjang,
                'tgl_daftar' : member.tgl_daftar,
                'status_aktif' : member.status_aktif,
                'segmentasi' : member.segmentasi,
                'pangkal' : member.pangkal.id_pk,
                'warga_media' : member.warga_media,
                'keterangan' : member.keterangan
            }
            return JsonResponse(data)