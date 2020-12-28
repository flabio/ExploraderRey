from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
# forms
from app.users.models import Perfil
from utilidades.utilidades import Utilidades
import  utilidades.validar as v
# Create your views here.

class userRepository:
    model = User
    model_perfil = Perfil
    model_util = Utilidades
        
    def get_perfil(self,pk):
        try:
            return Perfil.objects.get(user_id=pk)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    def listado_users(self,rol,*args, **kwargs):
        try:
            result = Perfil.objects.filter()
            return [{'pk': item.user.pk,
                        'id':item.perfil_id,
                        'foto':str( item.foto),
                        'nombre':v.validar_campo_string(item.user.first_name),
                        'apellidos': v.validar_campo_string(item.user.last_name),
                        'identificacion': item.identificacion,
                        'tipo_identificacion': item.tipo_identificacion,
                        'fecha_nacimiento':str(item.fecha_nacimiento),
                        'lugar_nacimiento':item.lugar_nacimiento,
                        'genero':item.genero,
                        'tipo_sangre':item.tipo_sangre,
                        'direccion': item.direccion,
                        'telefono': item.telefono,
                        'celular':item.celular,
                        'email': item.user.email,
                        'estado_civil':item.estado_civil,
                        'anion_conversion':item.anion_conversion,
                        'bautismo_agua':item.bautismo_agua,
                        'bautismo_espiritu':item.bautismo_espiritu,
                        'eps':v.validar_campo_string(item.eps.nombre),
                        'rol': v.validar_campo_string(item.user.groups.values('name')[0]['name'])} for item in result  if item.user.groups.values('name')[0]['name'] ==rol]
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
   
    def crear_users(self,request,rol,is_superuser, *args, **kwargs):
        try:
            
            if len(request.POST.get('first_name'))==0:
                return Utilidades.get_messages_400(self,'nombre')
               
            if len(request.POST.get('last_name')) == 0:
                return Utilidades.get_messages_400(self,'apellidos')
                
            if len(request.POST.get('identificacion'))==0:
                return Utilidades.get_messages_400(self,'identificacion')
                
            if len(request.POST.get('tipo_identificacion'))==0:
                return Utilidades.get_messages_400(self,'Tipo Identificación')
            
            if len(request.POST.get('fecha_nacimiento')) == 0:
                return Utilidades.get_messages_400(self,'fecha nacimiento')

            if len(request.POST.get('lugar_nacimiento')) == 0:
                return Utilidades.get_messages_400(self,'lugar nacimiento')
            
            if len(request.POST.get('estado_civil')) == 0:
                return Utilidades.get_messages_400(self,'estado civil')
            
            if len(request.POST.get('genero')) == 0:
                return Utilidades.get_messages_400(self,'genero')
            
            if len(request.POST.get('tipo_sangre'))==0:
                return Utilidades.get_messages_400(self,'tipo sangre')

            if len(request.POST.get('eps'))==0:
                return Utilidades.get_messages_400(self,'eps')

            if len(request.POST.get('direccion'))==0:
                return Utilidades.get_messages_400(self,'dirección')

            if len(request.POST.get('telefono'))==0:
                return Utilidades.get_messages_400(self,'teléfono')
            
            if len(request.POST.get('anion_conversion')) == 0:
                return Utilidades.get_messages_400(self,'año conversión')

            if len(request.POST.get('email')) == 0:
                return Utilidades.get_messages_400(self,'email')

            if rol!='admin':
                if len(request.POST.get('destacamento'))==0:
                    return Utilidades.get_messages_400(self,'destacamento')

            if len(request.POST.get('id'))==0:
                
                if len(request.POST.get('password1'))==0:
                    return Utilidades.get_messages_400(self,'contraseña')
            
                if len(request.POST.get('password2'))==0:
                    return Utilidades.get_messages_400(self,'confirma la contraseña')

                if  userRepository.get_queryset_Identificacion(self,request.POST.get('identificacion'))>0:
                    return Utilidades.gets_messages_400(self,'identificacion','El número de identificación ya existe')
                
                if userRepository.get_queryset_email(self,request.POST.get('email'))>0 :
                    return Utilidades.gets_messages_400(self,'email','El correo electrónico ya existe.')

            if Utilidades.calcular_ayer(self,request.POST.get('fecha_nacimiento'))<18 and request.POST.get('fecha_nacimiento') != None:
                return Utilidades.gets_messages_400(self,'Fecha Nacimiento','La edad debe ser igual a 18 o mayor, Fecha Nacimiento')
                
            
            if request.POST.get('password1')!=request.POST.get('password2'):
                return Utilidades.gets_messages_400(self,'contraseña','La contraseña no son igual.')
                 
            else:
                if len(request.POST.get('id'))>0:
                    user = User.objects.get(pk = request.POST.get('id'))
                else:
                    user = User.objects.create_user(username=request.POST.get('email'), password=request.POST['password1'])
               
                user.first_name     = request.POST.get('first_name')
                user.last_name      = request.POST.get('last_name')
                user.email          = request.POST.get('email')
                user.is_staff       = Utilidades.validar_estado(self,request.POST.get('is_staff'))
                user.is_active      = Utilidades.validar_estado(self,request.POST.get('estado'))
                user.is_superuser   = is_superuser
                user.save()
                result = userRepository.registrar_perfil(self,user,rol,request)
                if result>0:
                    return Utilidades.get_messages_200(self)
                else:
                    self.Eliminar(user.pk)
                    return Utilidades.get_messages_500(self,'Error, los datos se pueden guardar.')

        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))

    def Eliminar(self,pk):
        try:
            print(pk)
            object = Perfil.objects.get(user_id=pk)
            user = User.objects.get(pk=pk)
            user.delete()
            object.delete()

            return Utilidades.get_messages_elimino_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
        
    def registrar_perfil(self, user,rol, request):
        try:
            if len(request.POST.get('id'))>0:
                perfil = Perfil.objects.get(user_id=request.POST.get('id'))
            else:
                perfil = Perfil()
            
            if rol!='admin':
                perfil.Destacamento_id              = request.POST.get('destacamento')

            perfil.user_id                      = user.pk
            perfil.identificacion               = request.POST.get('identificacion')
            perfil.tipo_identificacion          = request.POST.get('tipo_identificacion')
            perfil.fecha_nacimiento             = request.POST.get('fecha_nacimiento')
            perfil.lugar_nacimiento             = request.POST.get('lugar_nacimiento')
            perfil.genero                       = request.POST.get('genero')
            perfil.tipo_sangre                  = request.POST.get('tipo_sangre')
            perfil.estado_civil                 = request.POST.get('estado_civil')
            
            perfil.eps_id                       = request.POST.get('eps')
            perfil.profesion                    = request.POST.get('profesion')
            perfil.direccion                    = request.POST.get('direccion')
            perfil.telefono                     = request.POST.get('telefono')
            perfil.celular                      = request.POST.get('celular')
            perfil.anion_conversion             = request.POST.get('anion_conversion')
            perfil.primaria_anio_cursado        = request.POST.get('primaria_anio_cursado')
            perfil.segundaria_anio_cursado      = request.POST.get('segundaria_anio_cursado')
            perfil.bautismo_agua                = Utilidades.validar_estado(self,request.POST.get('bautismo_agua'))
            perfil.bautismo_espiritu            = Utilidades.validar_estado(self,request.POST.get('bautismo_espiritu'))
            perfil.primaria                     = Utilidades.validar_estado(self,request.POST.get('primaria'))
            perfil.secundarias                  = Utilidades.validar_estado(self,request.POST.get('secundarias'))
            perfil.estado                       = Utilidades.validar_estado(self,request.POST.get('estado'))
            perfil.save()
            """grupo del usuario"""
            
            group = Group.objects.get(name=rol)
            
            if len(request.POST.get('id'))>0:
                user.groups.clear()
                user.groups.add(group)
            else:
                user.groups.add(group)
            
           
            return perfil.perfil_id
            
        except IntegrityError as error :
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def get_queryset_email(self, email):
        return User.objects.filter(email=email).count()

    def get_queryset_Identificacion(self, identificacion):
        return Perfil.objects.filter(identificacion=identificacion).count()
