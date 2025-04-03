from model.commands.PokemonCommand import PokemonCommand
from model.commands.RickCommand import RickCommand
from model.commands.GameCommand import GameCommand
from model.commands.StarCommand import StarCommand
from model.invokers.Invocadora import Invocadora
from model.receivers.ConsultaAPI import ConsultaAPI

A = ConsultaAPI

cmp = PokemonCommand(A,1)
cmr = RickCommand(A,1)
cmg = GameCommand(A,2)
cms = StarCommand(A,1)
s = Invocadora()

print(s.storeAndExecute(cmp))
print(s.storeAndExecute(cmr))
print(s.storeAndExecute(cmg))
print(s.storeAndExecute(cms))
print(s.lista)