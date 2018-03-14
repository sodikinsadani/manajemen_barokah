'''rest example'''

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from personalia.models import Individu
from django.shortcuts import get_object_or_404
from personalia.serializers import IndividuSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

class htmlRest(APIView):
    '''htmlRest'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'personalia/htmlrest.html'

    def get(self, request, pk = 16):
        '''get'''
        #queryset = Individu.objects.all()
        profile = get_object_or_404(Individu, pk=pk)
        serializer = IndividuSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk = 16):
        profile = get_object_or_404(Individu, pk=pk)
        raise Exception(request.data)
        serializer = IndividuSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return HttpResponseRedirect(reverse('personalia:htmlRest'))
        #return redirect('profile-list')

class htmlRestAjax(APIView):
    '''htmlRest'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'personalia/htmlrestajax.html'

    def get(self, request):
        '''get'''
        if self.request.is_ajax():
            status = request.GET['status']
            if status == 'View Edit':
                pk = request.GET['id']
                profile = get_object_or_404(Individu, pk=pk)
                serializer = IndividuSerializer(profile)
                #raise Exception(serializer)
                data = {
                    'status' : status,
                    'profile' : serializer.data,
                }
            return JsonResponse(data)
        else:
            serializer = IndividuSerializer()
            return Response({'serializer': serializer,})

    def post(self, request):
        status = request.POST['status']
        data = {
            'status' : status,
        }
        return JsonResponse(data)
