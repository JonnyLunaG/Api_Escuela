from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Escuela
import json

class EscuelaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            escuelas = list(Escuela.objects.filter(id=id).values())
            if len(escuelas)>0:
                escuela = escuelas[0] 
                datos = {'message': "Success", 'escuelas':escuela}
            else:
                datos = {'message': "Escuela no encontrada..."}
            return JsonResponse(datos)
        else: 
            escuelas = list(Escuela.objects.values())
            if len(escuelas)>0:
                datos = {'message': "Success", 'escuelas':escuelas}
            else:
                datos = {'message': "Escuelas no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Escuela.objects.create(nombre=jd['nombre'],telefono=jd['telefono'],nombre_rector=jd['nombre_rector'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        escuelas = list(Escuela.objects.filter(id=id).values())
        if len(escuelas)>0:
            escuela = Escuela.objects.get(id=id)  
            escuela.nombre = jd['nombre']
            escuela.telefono = jd['telefono']
            escuela.nombre_rector = jd['nombre_rector']
            escuela.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Escuela no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        escuelas = list(Escuela.objects.filter(id=id).values())
        if len(escuelas)>0:
            Escuela.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Escuela no encontrada..."}
        return JsonResponse(datos)
    



