from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
# forms

# Create your views here.

class groupsRepository:
    model = Group
   
    def listado_groups(self,*args, **kwargs):
        try:
            datos = []
            result = self.model.objects.all();
            for item in result:
                lista = {
                        'name': item.name,
                    }
                datos.append(lista)

            return datos;

        except IntegrityError as error:
            data = {
                'status':  500,
                'existe':  False,
                'estado':  'warning',
                'message': 'Error datos.'+str(error.args[1])
            }
            return data
    

    

    

    
    
