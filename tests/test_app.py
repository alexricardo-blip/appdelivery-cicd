import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import VERSAO

class TestAppDelivery(unittest.TestCase):
    def test_versao_existe(self):
        self.assertTrue(VERSAO)

    def test_versao_valida(self):
        self.assertRegex(VERSAO, r"^\d+\.\d+$")

if __name__ == "__main__":
    unittest.main()
