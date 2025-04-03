from model.interfaces.ICommand import ICommand

 
class PokemonCommand(ICommand):
    def __init__(self, cm,id):
        self.cm = cm
        self.id = id
    
    
    def execute(self):
        return self.cm.API_Pokemon(self.cm,self.id)
    
    pass