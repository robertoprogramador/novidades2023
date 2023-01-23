import unittest
from piloto import Piloto

class TestPilot(unittest.TestCase):
    def setUp(self):
        self.pilot1 = Piloto('airton','sena', 2000)
        self.pilot2 = Piloto('alan','Proust', 2000)
        self.pilot3 = Piloto('mauricio','Gugelmin', 500)

    def test_email(self):
        self.assertEqual(self.pilot1.email, 'airton.sena@email.com.br')
        self.assertEqual(self.pilot2.email, 'alan.Proust@email.com.br')
        self.assertEqual(self.pilot3.email, 'mauricio.Gugelmin@email.com.br')

        self.pilot3.nome ="Roberto"

        self.pilot3.sobrenome ="Pupomoreno"

    
        self.assertEqual(self.pilot3.email, 'Roberto.Pupomoreno@email.com.br')

    def test_nomecompleto(self): #testando a função que preenche o nome completo
        self.assertEqual(self.pilot1.nome_completo, 'airton sena') #o retorno
        self.assertEqual(self.pilot2.nome_completo, 'alan Proust')
        self.assertEqual(self.pilot3.nome_completo, 'mauricio Gugelmin')

    def test_aumentar_salario(self): #vamos aumentar o salario dos pilotos
        self.pilot1.aumentar_salario()
        self.pilot2.aumentar_salario()
        self.pilot3.aumentar_salario()

        self.assertEqual(self.pilot1.salario, 2200)
        self.assertEqual(self.pilot2.salario, 2200)
        self.assertEqual(self.pilot3.salario, 550)

#Este passo abaixo permite que sejam executados todos testes de uma só vez
if __name__ == '__main__':
    unittest.main()



