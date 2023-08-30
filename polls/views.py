from django.shortcuts import render


from .models import Oquv_markaz, oqituvchi
from django.http import JsonResponse


def all(request):
    jami=Oquv_markaz.objects.all()
    savelist =[]
    for i in jami:
        savelist.append({
            'name':i.name,
            'numbers of room':i.xonalar_soni
        })
    return JsonResponse(savelist, safe=False)
    
    


def detail(request, whichid):
    each = oqituvchi.objects.get(id=whichid)
    data={'O`qituvchi ismi':each.ismi, 'O`qituvchi nomeri':each.tel_nomer}
    return JsonResponse(data, safe=False)
