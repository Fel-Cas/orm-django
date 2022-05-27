from django.db import models
from django.db.models import Q
class AutorManager(models.Manager):
    """
    Operaciones en la base de datos para el modelo Autor
    """

    def listAuthors(self):
        return self.all()
    ## Es un filtro simple
    def findAuthor(self, keyword):
        return self.filter(
            ## Buscampos coincidencias, no que ssea igual estrictamente
            nombres__icontains=keyword
        )
    
    ##Buscamos el autor por el nombre y el apellido
    def findAuthorFullName(self, keyword):
        return self.filter(
            # Acá hacemos consultas haciendo O
            Q(nombres__icontains=keyword) | Q(apellidos__icontains=keyword)
        )
    ## Se utiliza el exlude para no traer los datos que no cumplan algun párametro
    def filterByEqualAge(self, keyword):
            return self.filter(
                nombres__icontains=keyword
            ).exclude(edad__gt=50)
    
    ## Hacemos el filtr mayor y menor que (> <)
    def filterByAge(self):
        return self.filter(
            edad__gt=30,
            edad__lt=60
        ).order_by('apellidos', 'nombres')