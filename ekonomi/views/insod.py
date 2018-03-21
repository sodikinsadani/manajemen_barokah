from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import render
from ekonomi.models import Insod
from ekonomi.forms import fInsod
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class insod(View):
    form_class = (fInsod)
    template_name = 'ekonomi/insod.html'

    def get_insod(self):
      insod = Insod.objects.all()
      return insod

    def get(self, request):
      context = {
          'insod' : self.get_insod(),
          'form' : self.form_class,
      }
      return render(request, self.template_name, context)

    def post(self, request):
      form = self.form_class(request.POST)
      #raise Exception(form.errors)
      if form.is_valid() :
          insod = form.save()
          messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data insod
          Silahkan input kembali data lainnya'''.format(insod.member.individu.nama.upper(),))
      else :
          messages.add_message(request, messages.WARNING, '''Gagal menambahkan data insod
          ''')
      return HttpResponseRedirect(reverse('ekonomi:insod'))

class insodEdit(View):
    form_class = (fInsod)

    def get_insod(self, pk):
        insod = get_object_or_404(Insod, pk=pk)
        return insod

    def post(self, request, pk):
        insod = self.get_insod(pk)

        nama_insod = insod.member.individu.nama
        form = self.form_class(request.POST, instance=insod)
        if form.is_valid() :
            insod = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} dari data insod
            '''.format(nama_insod,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data insod ''')

        return HttpResponseRedirect(reverse('ekonomi:insod'))

class insodDelete(View):
    def get_insod(self, pk):
        insod = get_object_or_404(Insod, pk=pk)
        return insod

    def post(self, request, pk):
        insod = self.get_insod(pk)
        nama_insod = insod.member.individu.nama
        try :
            insod = insod.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data insod
            '''.format(nama_insod,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data insod ''')

        return HttpResponseRedirect(reverse('ekonomi:insod'))
