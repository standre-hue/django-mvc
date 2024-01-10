from django.db import models
class DbContext:
    #models = []
    def __init__(self,*modelss):
        for model in modelss:
            if not isinstance( model, models.Model):
                print(type(model))
                #raise Exception("Arguments must be a Model Class")
            name = model.__name__.split('.')[-1]
            setattr(self, name, model)
        #self.models = models
        pass
    
