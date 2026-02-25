import unittest
import matplotlib.pyplot as plt
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):

    def setUp(self):
        self.ax = draw_plot()

    def test_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_x_label(self):
        self.assertEqual(self.ax.get_xlabel(), "Year")

    def test_y_label(self):
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_lines_exist(self):
        # There should be 2 regression lines
        self.assertEqual(len(self.ax.lines), 2)

    def test_line_extended_to_2050(self):
        line = self.ax.lines[0]
        x_data = line.get_xdata()
        self.assertEqual(max(x_data), 2050)

if __name__ == "__main__":
    unittest.main()