from model.interfaces.ICommand import ICommand

 
class GameCommand(ICommand):
    def __init__(self, cm,id):
        self.cm = cm
        self.id = id
    
    
    def execute(self):
        return self.cm.API_Ice_and_Fire(self.cm,self.id)
    
    
    pass