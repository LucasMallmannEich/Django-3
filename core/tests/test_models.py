import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico_teste = mommy.make('Servico')

    def test_str(self):
        self.assertEqual(str(self.servico_teste), self.servico_teste.servico)


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo_teste = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo_teste), self.cargo_teste.cargo)


class TeamTestCase(TestCase):
    def setUp(self):
        self.team_teste = mommy.make('Team')

    def test_str(self):
        self.assertEqual(str(self.team_teste), self.team_teste.nome)


class FeaturesTestCase(TestCase):
    def setUp(self):
        self.features_teste = mommy.make('Features')

    def test_str(self):
        self.assertEqual(str(self.features_teste), self.features_teste.nome)
