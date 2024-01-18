
import tkinter
from django.contrib import admin
from django.urls import path
from main.controllers.book_controller import BookController

from main.controllers.main_controller import MainController
from main.controllers.person_controller import PersonController
from main.database.dbcontext import DbContext
from main.models.Book import Book
from main.models.Person import Person

dbContext = DbContext(Person,Book)
mainController = MainController(dbContext=dbContext)
personController = PersonController(dbContext=dbContext)
bookController = BookController(dbContext=dbContext)

urlpatterns = [
    path('', mainController.index),
    path('list-person', personController.read, name='list-person'),
    path('create-person', personController.create, name='create-person'),
    path('delete-person', personController.delete, name='delete-person'),
    path('update-person/<int:pk>', personController.update, name='update-person'),
]
