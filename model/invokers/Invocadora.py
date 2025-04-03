class Invocadora:
    lista = []
    
    def storeAndExecute(self, cmd):
        self.lista.append(cmd.__class__.__name__)
        return cmd.execute()
        