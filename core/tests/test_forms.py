from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = 'Lucas Mallmann Eich'
        self.email = 'lucasmeich@gmail.com'
        self.assunto = 'Este é o assunto.'
        self.mensagem = 'Esta é a mensagem.'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # O mesmo que fazemos em "ContatoForm(request.POST)"

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        resposta1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        resposta2 = form2.send_mail()

        self.assertEquals(resposta1, resposta2)