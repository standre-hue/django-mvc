

from django.http import HttpResponse

from main.database.dbcontext import DbContext


class MainController:
    _dbContext = None
    def __init__(self,dbContext:DbContext):
        if not isinstance(dbContext, DbContext):
            raise Exception("Argument must be a DbContext class")
        self._dbContext = dbContext
        pass

    def index(self,request):
        #self._dbContext.models.
        print(self._dbContext.Person.objects.all())
        return HttpResponse('hello')

