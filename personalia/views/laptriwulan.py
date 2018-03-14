from django.shortcuts import render, get_object_or_404
from django.views import View
from enterprise.models import ParameterGlobal

class laporantriwulan(View):
    template_name = 'personalia/laporantriwulan.html'

    def get(self, request):
        triwulan = get_object_or_404(ParameterGlobal, pk=1)
        context = {
            'triwulan' : triwulan,
        }
        return render(request, self.template_name, context)
