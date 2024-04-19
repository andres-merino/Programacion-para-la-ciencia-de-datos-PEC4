from PEC4.Tarea1 import *
from PEC4.Tarea2 import *
from PEC4.Tarea3 import *
from PEC4.Tarea4 import *
from PEC4.Tarea5 import *
from PEC4.Tarea6 import *
from PEC4.Tarea7 import *

import unittest
import math
import os


class TestDataExpl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._df = lectura_archivo(os.path.join("data", "data.zip"))

    def test_Tarea1(self):
        self.assertEqual(self._df.shape, (35574, 32))

    def test_get_column_pandas(self):
        self.assertEqual(len(get_column_pandas("tracks_norm.csv", "track_id")),
                         35574)

    def test_get_column_byline(self):
        self.assertEqual(len(get_column_byline("tracks_norm.csv", "track_id")),
                         35574)

    def test_contar_valor(self):
        self.assertEqual(contar_valor(self._df, "name_artist", "Radiohead"),
                         159)

    def test_contar_contenido(self):
        self.assertEqual(contar_contenido(self._df, "name", "police"), 11)

    def test_contar_decada(self):
        self.assertEqual(contar_decada(self._df, 1990), 4638)

    def test_max_popularity(self):
        self.assertEqual(max_popularity(self._df, 10), "Beggin'")

    def test_all_decades(self):
        self.assertEqual(len(all_decades(self._df, 1960)), 4)

    def test_dist_euclidea(self):
        self.assertEqual(dist_euclidea([1, 0], [0, 1]), math.sqrt(2))

    def test_dist_cousinus(self):
        self.assertEqual(dist_cousinus([1, 0], [0, 1]), 0)

    def test_max_min_mean_energy(self):
        estadisticas = max_min_mean_energy(self._df, "Metallica")
        self.assertEqual(estadisticas[0], 0.998)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataExpl)
unittest.TextTestRunner(verbosity=2).run(suite)
