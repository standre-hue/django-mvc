from django.forms import ModelForm

from main.models.Person import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"