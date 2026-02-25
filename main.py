import unittest
from sea_level_predictor import draw_plot

# Run the function
draw_plot()

# Run unit tests
loader = unittest.TestLoader()
suite = loader.discover('.', pattern='test_module.py')

runner = unittest.TextTestRunner()
runner.run(suite)