from model.interfaces.ICommand import ICommand

 
class StarCommand(ICommand):
    def __init__(self, cm,id):
        self.cm = cm
        self.id = id
    
    
    def execute(self):
        return self.cm.API_Star_Wars(self.cm,self.id)
    
    pass