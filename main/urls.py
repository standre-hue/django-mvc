
import tkinter
from django.contrib import admin
from django.urls import path

from main.controllers.main_controller import MainController
from main.database.dbcontext import DbContext
from main.models.Book import Book
from main.models.Person import Person

dbContext = DbContext(Person,Book)
mainController = MainController(dbContext=dbContext)

urlpatterns = [
    path('', mainController.index),
]
