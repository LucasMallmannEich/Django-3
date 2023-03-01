from django.test import TestCase
from django.test import Client  # Client executa verbos HTTP.
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Lucas',
            'email': 'lme@gmail.com',
            'assunto': 'Assunto',
            'mensagem': 'esta eh minha mensagem!'
        }

    def test_form_valid(self):
        request = Client().post(reverse_lazy('rota_index'), data=self.dados)
        self.assertEquals(request.status_code, 302)  # Se o form for válido, há o código HTTP 302 (redirect).

    def test_form_invalid(self):
        dados = {
            'nome': 'Lucas',
        }
        request = Client().post(reverse_lazy('rota_index'), data=dados)
        self.assertEquals(request.status_code, 200)  # Se o form for inválido, há o código HTTP 200.
