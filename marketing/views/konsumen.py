from django.shortcuts import render, get_object_or_404
from django.views import View
from marketing.models import Konsumen
from marketing.forms import fKonsumen
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from personalia.forms import fIndividu
from personalia.models import Individu
from django.db import transaction
import datetime
from personalia.models import Member
from django.utils import timezone

class konsumen(View):
    form_class = (fIndividu,fKonsumen)
    template_name = 'marketing/konsumen.html'

    def get_konsumen(self):
        konsumen = Konsumen.objects.all().exclude(status='9')
        return konsumen

    def get(self, request):
        context = {
            'konsumen' : self.get_konsumen(),
            'form' : self.form_class,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form1 = self.form_class[0](request.POST)
        form2 = self.form_class[1](request.POST)

        if form1.is_valid() and form1.is_valid():
            with transaction.atomic():
                individu = form1.save()
                konsumen = form2.save(commit=False)
                konsumen.individu = individu
                konsumen.save()
                messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data konsumen
                Silahkan input kembali data lainnya'''.format(individu.nama.upper(),))
        else :
            form = (form1,form2)
            individu = form1.clean()
            messages.add_message(request, messages.WARNING, '''Gagal menambahkan {0} ke dalam data konsumen
            '''.format(individu['nama'].upper(),))
        return HttpResponseRedirect(reverse('marketing:konsumen'))

class konsumenEdit(View):
    form_class = (fIndividu,fKonsumen)

    def get_individu(self, pk):
        individu = get_object_or_404(Individu, pk=pk)
        return individu

    def get_konsumen(self, pk):
        konsumen = get_object_or_404(Konsumen, pk=pk)
        return konsumen

    def post(self, request, pk):
        individu = self.get_individu(pk)
        konsumen = self.get_konsumen(pk)
        nama_konsumen = konsumen.individu.nama
        form1 = self.form_class[0](request.POST, instance=individu)
        form2 = self.form_class[1](request.POST, instance=konsumen)

        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                individu = form1.save()
                konsumen = form2.save()
                messages.add_message(request, messages.SUCCESS, '''
                Berhasil mengubah data {0} dari data konsumen
                '''.format(nama_konsumen,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data konsumen ''')

        return HttpResponseRedirect(reverse('marketing:konsumen'))

class konsumenDelete(View):
    def get_individu(self, pk):
        individu = get_object_or_404(Individu, pk=pk)
        return individu

    def post(self, request, pk):
        individu = self.get_individu(pk)
        nama_individu = individu.nama

        try :
            individu = individu.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data konsumen
            '''.format(nama_individu,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data konsumen ''')

        return HttpResponseRedirect(reverse('marketing:konsumen'))

class konsumenFinish(View):
    form_class = (fIndividu,fKonsumen)

    def get_individu(self, pk):
        individu = get_object_or_404(Individu, pk=pk)
        return individu

    def get_konsumen(self, pk):
        konsumen = get_object_or_404(Konsumen, pk=pk)
        return konsumen

    def post(self, request, pk):
        individu = self.get_individu(pk)
        nama_konsumen = individu.nama

        '''konsumen = self.get_konsumen(pk)
        raise Exception(konsumen.warga_media)'''
        try :
            konsumen = self.get_konsumen(pk)
            konsumen.status = '9'
            tgl_finish = request.POST['tgl_finish'].split('/')
            tgl_finish = datetime.date(int(tgl_finish[2]), int(tgl_finish[0]), int(tgl_finish[1]))
            konsumen.tgl_finish = tgl_finish
            konsumen.save()

            member = Member(
                individu = individu, jenjang='0', tgl_daftar=tgl_finish,
                status_aktif=konsumen.status_aktif,segmentasi=konsumen.segmentasi,
                pangkal=konsumen.sales.sales_id.pangkal,warga_media=konsumen.warga_media,
                keterangan=konsumen.keterangan#,tgl_input=timezone.now()
            )
            member.save()

            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} menjadi data finish
            '''.format(nama_konsumen,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data finish ''')

        return HttpResponseRedirect(reverse('marketing:konsumen'))
