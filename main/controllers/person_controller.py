from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from main.controllers.base_controller import BaseController
from main.database.dbcontext import DbContext
from main.views.forms.person_form import PersonForm


class PersonController(BaseController):

    def __init__(self,dbContext:DbContext):
        super().__init__(dbContext)

    def create(self,request):
        #self._dbContext.models.
        #print(self._dbContext.Person.objects.all())
        form = PersonForm()
        context = { 'form':form }
        if request.method == 'POST':
            person_data = PersonForm(request.POST)
            if person_data.is_valid():
                person_data.save()
                return redirect(reverse_lazy('list-person'))
            else:
                print(person_data.errors)

        return render(request,'create_person.html',context)
       
    
    def update(self,request,pk):
        #author = get_object_or_404(self._dbContext.Person, pk=pk)
        author = self._dbContext.Person.objects.get(pk=pk)
        form = PersonForm({'name':author.name, 'age':author.age})
        context = { 'form': form}
        if request.method == 'POST':
            author.name = request.POST['name']
            author.age = request.POST['age']
            author.save()
            return redirect(reverse_lazy('list-person'))
            '''person_data = PersonForm(request.POST)
            if person_data.is_valid():
                person_data.save()
                return redirect(reverse_lazy('list-person'))
            else:
                print(person_data.errors)
            '''
        return render(request,'update_person.html',context)
        pass

    def read(self,request):
        authors = self._dbContext.Person.objects.all()
        context = { 'authors':authors }
        return render(request,'list_person.html',context)
        

    def delete(self,request):
        pass

