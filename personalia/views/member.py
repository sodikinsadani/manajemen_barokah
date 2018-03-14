from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from personalia.forms import fIndividu,fMember
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from personalia.models import Member,Individu

class member(View):
    form_class = (fIndividu,fMember)
    template_name = 'personalia/member.html'

    def get_member(self):
        member = Member.objects.all()
        return member

    def get(self, request):
        context = {
            'member' : self.get_member(),
            'form' : self.form_class,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form1 = self.form_class[0](request.POST)
        form2 = self.form_class[1](request.POST)

        if form1.is_valid() and form1.is_valid():
            with transaction.atomic():
                individu = form1.save()
                warga = form2.save(commit=False)
                warga.individu = individu
                warga.save()
                messages.add_message(request, messages.SUCCESS, '''Berhasil menambah {0} ke dalam data member
                Silahkan input kembali data lainnya'''.format(individu.nama.upper(),))
        else :
            form = (form1,form2)
            individu = form1.clean()
            messages.add_message(request, messages.WARNING, '''Gagal menambahkan {0} ke dalam data member
            '''.format(individu['nama'].upper(),))
        return HttpResponseRedirect(reverse('personalia:member'))

class memberEdit(View):
    form_class = (fIndividu,fMember)

    def get_individu(self, pk):
        individu = get_object_or_404(Individu, pk=pk)
        return individu

    def get_member(self, pk):
        member = get_object_or_404(Member, pk=pk)
        return member

    def post(self, request, pk):
        individu = self.get_individu(pk)
        member = self.get_member(pk)
        nama_member = member.individu.nama
        form1 = self.form_class[0](request.POST, instance=individu)
        form2 = self.form_class[1](request.POST, instance=member)

        if form1.is_valid() and form2.is_valid():
            with transaction.atomic():
                individu = form1.save()
                member = form2.save()
                messages.add_message(request, messages.SUCCESS, '''
                Berhasil mengubah data {0} dari data member
                '''.format(nama_member,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data member ''')

        return HttpResponseRedirect(reverse('personalia:member'))

class memberDelete(View):
    def get_individu(self, pk):
        individu = get_object_or_404(Individu, pk=pk)
        return individu

    def post(self, request, pk):
        individu = self.get_individu(pk)
        nama_individu = individu.nama

        try :
            individu = individu.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data member
            '''.format(nama_individu,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data member ''')

        return HttpResponseRedirect(reverse('personalia:member'))
