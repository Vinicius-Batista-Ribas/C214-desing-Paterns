import sys
import unittest
from io import StringIO
from unittest.mock import patch
from Observer import CapsLockOn, PalavrasCont, PalavrasPar, TotalPalavras

class TestContadorPalavras(unittest.TestCase):
    def setUp(self):
        self.contador = PalavrasCont()

    def TestContaPalavras(self):
        allWords = TotalPalavras()
        self.contador.adicionaObservador(allWords)
        phrase = "Teste de observador de palavras"
        expected_output = "Total de palavras: 5\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contador.frase(phrase)
            self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_total_palavras_observer_caso_negativo(self):
        allWords = TotalPalavras()
        self.contador.adicionaObservador(allWords)
        phrase = "Teste de observador de palavras"
        expected_output = "Total de palavras: 10\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contador.frase(phrase)
            self.assertNotEqual(mock_stdout.getvalue(), expected_output)

    def TestPalavrasPares(self):
        palavrasPares = PalavrasPar()
        self.contador.adicionaObservador(palavrasPares)
        phrase = "Teste de palavras com comprimento par"
        expected_output = "Palavras com comprimento par: 4\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contador.frase(phrase)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def TestPalavrasCaps(self):
        capsWords = CapsLockOn()
        self.contador.adicionaObservador(capsWords)
        phrase = "Teste de Caps Lock em Palavras"
        expected_output = "Palavras começadas com maiúsculas: 2\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.contador.frase(phrase)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def capture_stdout(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        return captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()