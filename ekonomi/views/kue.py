from django.shortcuts import render, get_object_or_404
from django.views import View
from ekonomi.models import Kue, Penjualan
from ekonomi.forms import fKue, fPenjualanKue
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class UpdateStok:

    def get_kue(self, pk):
        kue = get_object_or_404(Kue, pk=pk)
        return kue

    def update_stok(self,params):
        kue = self.get_kue(params.kue.id)
        if params.jenis_transaksi == '1':
            terjual = kue.terjual + params.jumlah
            kue.terjual = terjual
        elif params.jenis_transaksi == '2':
            terjual = kue.terjual - params.jumlah
            kue.terjual = terjual
        elif params.jenis_transaksi == '3':
            stok = kue.stok - params.jumlah
            kue.stok = stok
        elif params.jenis_transaksi == '4':
            stok = kue.stok + params.jumlah
            kue.stok = stok
        else :
            raise Exception('errors update_stok')
        kue.save()

    def update_delete(self,params):
        kue = self.get_kue(params.kue.id)
        if params.jenis_transaksi == '1':
            terjual = kue.terjual - params.jumlah
            kue.terjual = terjual
        elif params.jenis_transaksi == '2':
            terjual = kue.terjual + params.jumlah
            kue.terjual = terjual
        elif params.jenis_transaksi == '3':
            stok = kue.stok + params.jumlah
            kue.stok = stok
        elif params.jenis_transaksi == '4':
            stok = kue.stok - params.jumlah
            kue.stok = stok
        else :
            raise Exception('errors update_delete')
        kue.save()

    def update_update(self,params,jenis_transaksi):
        kue = self.get_kue(params.kue.id)
        if jenis_transaksi == '1':
            terjual = kue.terjual - params.jumlah
            kue.terjual = terjual
        elif jenis_transaksi == '2':
            terjual = kue.terjual + params.jumlah
            kue.terjual = terjual
        elif jenis_transaksi == '3':
            stok = kue.stok + params.jumlah
            kue.stok = stok
        elif jenis_transaksi == '4':
            stok = kue.stok - params.jumlah
            kue.stok = stok
        else :
            raise Exception('errors update_delete')
        kue.save()

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

class penjualanKue(View):
    form_class = (fPenjualanKue)
    template_name = 'ekonomi/penjualan_kue.html'

    def get_penjualan(self):
      penjualan = Penjualan.objects.all()
      return penjualan

    def get(self, request):
      context = {
          'penjualan' : self.get_penjualan(),
          'form' : self.form_class,
      }
      return render(request, self.template_name, context)

    def post(self, request):
      form = self.form_class(request.POST)
      #raise Exception(form.errors)
      if form.is_valid() :
          penjualan = form.save()
          update_stok = UpdateStok()
          update_stok.update_stok(penjualan)
          messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data transaksi penjualan
          Silahkan input kembali data lainnya'''.format(penjualan.nama_konsumen.upper(),))
      else :
          messages.add_message(request, messages.WARNING, '''Gagal menambahkan data transaksi penjualan
          ''')
      return HttpResponseRedirect(reverse('ekonomi:penjualankue'))

class penjualankueEdit(View):
    form_class = (fPenjualanKue)

    def get_penjualan_kue(self, pk):
        penjualan = get_object_or_404(Penjualan, pk=pk)
        return penjualan

    def post(self, request, pk):
        penjualan = self.get_penjualan_kue(pk)
        jumlah = penjualan.jumlah
        jenis_transaksi = penjualan.jenis_transaksi

        nama_penjualan = penjualan.nama_konsumen
        form = self.form_class(request.POST, instance=penjualan)
        if form.is_valid() :
            penjualan = form.save()
            update_stok = UpdateStok()
            if penjualan.jenis_transaksi == jenis_transaksi :
                penjualan.jumlah = penjualan.jumlah - jumlah
            else :
                update_stok.update_update(penjualan,jenis_transaksi)
            update_stok.update_stok(penjualan)
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} dari data transaksi penjualan kue
            '''.format(nama_penjualan,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data transaksi penjualan kue ''')

        return HttpResponseRedirect(reverse('ekonomi:penjualankue'))

class penjualankueDelete(View):
    def get_penjualan_kue(self, pk):
        penjualan = get_object_or_404(Penjualan, pk=pk)
        return penjualan

    def post(self, request, pk):
        penjualan = self.get_penjualan_kue(pk)
        params = penjualan
        nama_penjualan = penjualan.nama_konsumen
        try :
            penjualan = penjualan.delete()
            update_stok = UpdateStok()
            update_stok.update_delete(params)
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data transaksi penjualan kue
            '''.format(nama_penjualan,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data tranasaksi penjualan kue ''')

        return HttpResponseRedirect(reverse('ekonomi:penjualankue'))
