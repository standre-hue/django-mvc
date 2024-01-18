

from django.http import HttpResponse
from main.controllers.base_controller import BaseController

from main.database.dbcontext import DbContext


class MainController(BaseController):

    def __init__(self,dbContext:DbContext):
        super().__init__(dbContext)

    def index(self,request):
        #self._dbContext.models.
        print(self._dbContext.Person.objects.all())
        return HttpResponse('hello')

