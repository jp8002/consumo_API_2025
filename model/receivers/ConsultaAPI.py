from abc import ABCMeta, abstractmethod
import requests

class ConsultaAPI():
    
    def API_Pokemon(self, id):
        URL = 'https://pokeapi.co/api/v2/pokemon/'
        
        URL = URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

    def API_Rick_Morty(self, id):
    
        URL = 'https://rickandmortyapi.com/api/character/'

        try:
            URL += str(id)
            dado = requests.get(URL).json()
            return (dado.get("id"),dado.get("name"),dado.get("species"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
            
        pass

    def API_Star_Wars(self, id):
        ''' The universe of Star Wars '''
        URL = 'https://swapi.dev/api/people/'
        try:
            URL += str(id)
            dado = requests.get(URL).json()
            return (dado.get("name"), dado.get("films"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
        pass

    def API_Ice_and_Fire(self, id):
        
        URL = 'https://anapioficeandfire.com/api/characters/'
        try:
            URL += str(id)
            dado = requests.get(URL).json()
            return (dado.get("name"), dado.get("tvSeries"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
        pass
 