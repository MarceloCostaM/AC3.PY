class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso

class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso):
        super().__init__(instituicao, curso)
        self.__argumentos = None

    def get_curso(self):
        print('doutorado em ', self.curso)

    def get_tese(self):
        return self.__tese

    def set_tese(self, titulo):
        self.__tese = titulo

    def exibir(self):
        
        print('instituiçao: ', self.instituicao)
        print('cuso: ', self.curso)
        print('Tese: ', self.__tese)


print('-'*160)
doc = Doutorado('impacta', 'Análise e Desenvolvimento de Sistemas')
doc.get_curso()
doc.set_tese("Insigne em Programação orientada a Objetos")
doc.exibir()
print('titulo da tese: ' , doc.get_tese())
