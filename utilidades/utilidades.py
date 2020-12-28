from django.http import JsonResponse,HttpResponse
from datetime import datetime, date, time, timedelta
class Utilidades:
    """Valica contraseña"""
    def calcular_ayer(self,fecha):
        ahora = datetime.strptime(fecha,'%Y-%m-%d')
        fecha_auctual = datetime.now()
        year = fecha_auctual.year-ahora.year
        return year

    def validar_estado(self,estado):
        if estado == 'true':
            return 1
        else:
            return 0
    def Comparar_password(self,request):

        if request.POST.get('password1') != request.POST.get('password2'):
            data = {
                'status':'200',
                'existe':True,
                'estado':'warning',
                'message':'La contraseña son diferente.'
            }
            return data


    def vacia_campo_requerido(request):
        
        if request.POST.get('first_name') is None:
            data = {
                'status':'200',
                'existe':True,
                'estado':'warning',
                'message':'El campo nombre es requeridad.'
            }

            return data
    def get_messages_200(self):
        data = {
           'status': 200,
           'existe': True,
           'estado': 'success',
           'message':'Los datos se guardo exitosamente.'
            }
        return data
    def get_messages_elimino_200(self):
        data = {
           'status': 200,
           'existe': True,
           'estado': 'success',
           'message':'El registro se elimino exitosamente.'
            }
        return data

    def get_messages_400(self,variable):
        
        data = {
           'status': 400,
           'existe': False,
           'title':  variable.capitalize(),
           'estado': 'warning',
           'message': format(variable)
            }
        return data
    
    def get_messages_mayor_cero_400(self):
        
        data = {
           'status': 400,
           'existe': False,
           'title':  'Mayor que cero',
           'estado': 'warning',
           'message': 'The value must be greater than 0'
            }
        return data
    def gets_messages_400(self,variable,msg):
        data = {
           'status': 400,
           'existe': False,
           'title':  variable.capitalize(),
           'estado': 'warning',
           'message': msg
            }
        return data

    def get_messages_500(self,msg):
        data = {
           'status': 500,
           'existe': False,
           'estado': 'error',
           'message':'Error de services'+str(msg)
            }
        return data

    