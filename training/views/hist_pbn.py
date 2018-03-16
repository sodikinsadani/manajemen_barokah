from training.models import Histpbn
from django.shortcuts import render, get_object_or_404
from django.views import View
from training.forms import fHistpbn
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class hist_pbn(View):
    form_class = (fHistpbn)
    template_name = 'training/hist_pbn.html'

    def get_hist_pbn(self):
        hist_pbn = Histpbn.objects.all()
        return hist_pbn

    def get(self, request):
        context = {
            'hist_pbn' : self.get_hist_pbn(),
            'form' : self.form_class,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid() :
            hist_pbn = form.save()
            messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data histori training
            Silahkan input kembali data lainnya'''.format(hist_pbn.peserta.id_peserta.individu.nama.upper(),))
        else :
            messages.add_message(request, messages.WARNING, '''Gagal menambahkan data histori training
            ''')
        return HttpResponseRedirect(reverse('training:hist_pbn'))

class hist_pbnEdit(View):
    form_class = (fHistpbn)

    def get_hist_pbn(self, pk):
        hist_pbn = get_object_or_404(Histpbn, pk=pk)
        return hist_pbn

    def post(self, request, pk):
        hist_pbn = self.get_hist_pbn(pk)

        nama_peserta = hist_pbn.peserta.id_peserta.individu.nama
        form = self.form_class(request.POST, instance=hist_pbn)
        if form.is_valid() :
            hist_pbn = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} dari data histori training
            '''.format(nama_peserta,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data histori training ''')

        return HttpResponseRedirect(reverse('training:hist_pbn'))

class hist_pbnDelete(View):
    def get_hist_pbn(self, pk):
        hist_pbn = get_object_or_404(Histpbn, pk=pk)
        return hist_pbn

    def post(self, request, pk):
        hist_pbn = self.get_hist_pbn(pk)
        nama_peserta = hist_pbn.peserta.id_peserta.individu.nama
        try :
            hist_pbn = hist_pbn.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data histori training
            '''.format(nama_peserta,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data histori training ''')

        return HttpResponseRedirect(reverse('training:hist_pbn'))
