from django.shortcuts import render


from .models import Oquv_markaz, oqituvchi
from django.http import JsonResponse
from .serializer import OquvmarkazSerializer, oqituvchiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# def all(request):
#     jami=Oquv_markaz.objects.all()
#     savelist = OquvmarkazSerializer(jami, many=True)
#     # for i in jami:
#     #     savelist.append({
#     #         'name':i.name,
#     #         'numbers of room':i.xonalar_soni
#     #     })
#     return JsonResponse(savelist.data, safe=False)

class getOquvMarkaz(APIView):
    def get(self, request):
        bor = Oquv_markaz.objects.all()
        srr2=OquvmarkazSerializer(bor, many=True)
        return Response(srr2.data)
    
    


def detail(request, whichid):
    each=oqituvchi.objects.filter(id=whichid)
    ss=oqituvchiSerializer(each, many=True)
    # each = oqituvchi.objects.get(id=whichid)
    # data={'O`qituvchi ismi':each.ismi, 'O`qituvchi nomeri':each.tel_nomer}
    return JsonResponse(ss.data, safe=False)


class postoquvmarkaz(APIView):
    def post(self, request):
        main_body=request.data
        sss = OquvmarkazSerializer(data=main_body)
        if sss.is_valid():
            sss.save()
            return Response(sss.data)
        return Response(sss.errors)
