from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import psycopg2

class index(View):
    template_name = 'enterprise/index.html'

    def get(self, request):
        return render(request, self.template_name)

class getDataChart(View):
    def db_server(self):
        try:
            conn = psycopg2.connect("dbname='barokah' user='sodikin' host='localhost' password='nurs4d4ni'")
            return conn
        except:
            print("I am unable to connect to the database")

    def get(self, request):
        conn = self.db_server()
        cur = conn.cursor()
        #member aktif
        cur.execute('''
            select
            count(
                case
                    when m.jenjang = '0' then '1'
                end
            ) as wb,
            count(
                case
                    when m.jenjang = '1' then '1'
                end
            ) as pra,
            count(
                case
                    when m.jenjang in ('2','3','4') then '1'
                end
            ) as a1,
            count(
                case
                    when m.jenjang = '5' then '1'
                end
            ) as a2
            from barokah.personalia_member m
            where m.status_aktif='ak'
        ''')
        p = cur.fetchall()[0]

        data = {
        'personalia' : {
            "WB Aktif" : p[0],
            "PRA A1 Aktif" : p[1],
            "A1 Aktif" : p[2],
            "A2 Aktif" : p[3]
        }, }
        return JsonResponse(data)
