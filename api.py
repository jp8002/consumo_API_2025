from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        try:
            self.__URL += str(id)
            dado = requests.get(self.__URL).json()
            return (dado.get("id"),dado.get("name"),dado.get("species"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
        pass

class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        try:
            self.__URL += str(id)
            dado = requests.get(self.__URL).json()
            return (dado.get("name"), dado.get("films"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
        pass

class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        try:
            self.__URL += str(id)
            dado = requests.get(self.__URL).json()
            return (dado.get("name"), dado.get("tvSeries"))
        except Exception as e:
            print("OCORREU UM ERRO:", e)
        pass
 