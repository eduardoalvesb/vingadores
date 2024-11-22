

class Humano(Vingador): 
    def __init__(self, nome_heroi, nome_real, poderes, poder_principal, fraquezas, nivel_forca):
        super().__init__(nome_heroi, nome_real, 'Humano', poderes, poder_principal, fraquezas, nivel_forca)
 
class MetaHumano(Vingador):  
    def __init__(self, nome_heroi, nome_real, poderes, poder_principal, fraquezas, nivel_forca):
        super().__init__(nome_heroi, nome_real, 'Meta-Humano', poderes, poder_principal, fraquezas, nivel_forca)
 
class Alienigena(Vingador):  
    def __init__(self, nome_heroi, nome_real, poderes, poder_principal, fraquezas, nivel_forca):
        super().__init__(nome_heroi, nome_real, 'Alienígena', poderes, poder_principal, fraquezas, nivel_forca)
 
class Deus(Vingador): 
    def __init__(self, nome_heroi, nome_real, poderes, poder_principal, fraquezas, nivel_forca):
        super().__init__(nome_heroi, nome_real, 'Deus', poderes, poder_principal, fraquezas, nivel_forca)