import datetime
from django.db import models
 
class LibroManager(models.Manager):
    """
    Manager para el modelo Libro
    """
    
    def getAll(self):
        return self.all()
    
    def filterByDate(self, keyword):
        return self.filter(
            titulo__icontains=keyword,
            fecha__range=('2000-01-01', '2021-12-31')
        )
    def filterByDate1(self, keyword, startDate, finishDate):
        return self.filter(
            titulo__icontains=keyword,
            ## Converimos las fechas al formato correcto
            fecha__range=(datetime.datetime.strptime(  startDate,'%Y-%m-%d').date(), datetime.datetime.strptime(finishDate,'%Y-%m-%d').date())
        )
