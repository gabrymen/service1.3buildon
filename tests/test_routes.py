import unittest
from dotenv import load_dotenv
import os
import sys

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Aggiungi il percorso del progetto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.getenv('PYTHONPATHREPO')))

from app import create_app
from config import TestingConfig

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestingConfig)
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Welcome to the ML Clustering Service', response.data)

    def test_preprocess(self):
        response = self.client.post('/api/preprocess', json={"your": "data"})
        self.assertEqual(response.status_code, 200)

    def test_cluster(self):
        response = self.client.post('/api/cluster', json={"your": "data"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
