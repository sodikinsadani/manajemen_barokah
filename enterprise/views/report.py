from django.shortcuts import render,get_object_or_404
from django.views import View
from enterprise.models import Report
from django.http import HttpResponse
from datetime import datetime as dt
from enterprise.script import detil_member

class report(View):
    template_name = 'enterprise/report.html'

    def get_report(self):
        report = Report.objects.filter(is_enable=True).order_by('app','nama_laporan',)
        return report

    def get(self, request):
        context = {
            'report' : self.get_report(),
        }

        return render(request, self.template_name, context)

class reportdownload(View):
    query = {
        'detil_member':detil_member.ConstructReport
    }

    def get(self, request, pk):
        rep = get_object_or_404(Report,pk=pk)
        date_now = dt.today().strftime("%d%m%y %H:%M:%S")

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename={nama_laporan} {date_now}.xlsx \
        '.format(**{'nama_laporan':rep.nama_laporan, 'date_now':date_now})

        response = self.query[rep.script](response, rep)
        return response
