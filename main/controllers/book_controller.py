from django.http import HttpResponse
from main.controllers.base_controller import BaseController
from main.database.dbcontext import DbContext


class BookController(BaseController):

    def __init__(self,dbContext:DbContext):
        super().__init__(dbContext)

    def create(self,request):
        #self._dbContext.models.
        print(self._dbContext.Person.objects.all())
        return HttpResponse('hello')
    
    def update(self,request):
        pass

    def read(self,request):
        pass

    def delete(self,request):
        pass

