from django.shortcuts import render, get_object_or_404
from django.views import View
from ekonomi.models import Kue
from ekonomi.forms import fKue
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class kue(View):
    form_class = (fKue)
    template_name = 'ekonomi/kue.html'

    def get_kue(self):
      kue = Kue.objects.all()
      return kue

    def get(self, request):
      context = {
          'kue' : self.get_kue(),
          'form' : self.form_class,
      }
      return render(request, self.template_name, context)

    def post(self, request):
      form = self.form_class(request.POST)
      #raise Exception(form.errors)
      if form.is_valid() :
          kue = form.save()
          messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data kue
          Silahkan input kembali data lainnya'''.format(kue.nama_kue.upper(),))
      else :
          messages.add_message(request, messages.WARNING, '''Gagal menambahkan data kue
          ''')
      return HttpResponseRedirect(reverse('ekonomi:kue'))

class kueEdit(View):
    form_class = (fKue)

    def get_kue(self, pk):
        kue = get_object_or_404(Kue, pk=pk)
        return kue

    def post(self, request, pk):
        kue = self.get_kue(pk)

        nama_kue = kue.nama_kue
        form = self.form_class(request.POST, instance=kue)
        if form.is_valid() :
            kue = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} dari data kue
            '''.format(nama_kue,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data kue ''')

        return HttpResponseRedirect(reverse('ekonomi:kue'))

class kueDelete(View):
    def get_kue(self, pk):
        kue = get_object_or_404(Kue, pk=pk)
        return kue

    def post(self, request, pk):
        kue = self.get_kue(pk)
        nama_kue = kue.nama_kue
        try :
            kue = kue.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data kue
            '''.format(nama_kue,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data kue ''')

        return HttpResponseRedirect(reverse('ekonomi:kue'))
