from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from personalia.forms import fIndividu

@method_decorator(login_required, name='dispatch')
class classBase(View):
    greeting = "Good Day"

    def get(self, request):
        # <view logic>
        return HttpResponse(self.greeting)


class classBase2(classBase):
    greeting = "Morning to ya"

class classBase3(View):
    form_class = fIndividu
    initial = {'nama': 'sodikin'}
    template_name = 'personalia/classbase3.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
