from model.interfaces.ICommand import ICommand

 
class RickCommand(ICommand):
    def __init__(self, cm,id):
        self.cm = cm
        self.id = id
    
    
    def execute(self):
        return self.cm.API_Rick_Morty(self.cm,self.id)
    
    pass