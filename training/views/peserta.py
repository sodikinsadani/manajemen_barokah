from django.shortcuts import render, get_object_or_404
from django.views import View
from training.models import Peserta
from training.forms import fPeserta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class peserta(View):
    form_class = (fPeserta)
    template_name = 'training/peserta.html'

    def get_peserta(self):
        peserta = Peserta.objects.all()
        return peserta

    def get(self, request):
        context = {
            'peserta' : self.get_peserta(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid() :
            peserta = form.save()
            messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data peserta
            Silahkan input kembali data lainnya'''.format(peserta.id_peserta.individu.nama.upper(),))
        else :
            messages.add_message(request, messages.WARNING, '''Gagal menambahkan data peserta
            ''')
        return HttpResponseRedirect(reverse('training:peserta'))

class pesertaEdit(View):
    form_class = (fPeserta)

    def get_peserta(self, pk):
        peserta = get_object_or_404(Peserta, pk=pk)
        return peserta

    def post(self, request, pk):
        peserta = self.get_peserta(pk)

        nama_peserta = peserta.id_peserta.individu.nama
        form = self.form_class(request.POST, instance=peserta)
        if form.is_valid() :
            peserta = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} dari data peserta
            '''.format(nama_peserta,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data peserta ''')

        return HttpResponseRedirect(reverse('training:peserta'))

class pesertaDelete(View):
    def get_peserta(self, pk):
        peserta = get_object_or_404(Peserta, pk=pk)
        return peserta

    def post(self, request, pk):
        peserta = self.get_peserta(pk)
        nama_peserta = peserta.id_peserta.individu.nama
        try :
            peserta = peserta.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data peserta
            '''.format(nama_peserta,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data peserta ''')

        return HttpResponseRedirect(reverse('training:peserta'))
