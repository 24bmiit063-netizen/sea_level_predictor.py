import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Import data
    df = pd.read_csv( "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # -------- First line of best fit (1880–2050) --------
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create years up to 2050
    years_extended = np.arange(df['Year'].min(), 2051)

    # Predict sea levels
    sea_levels_predicted = result.slope * years_extended + result.intercept

    # Plot line
    plt.plot(years_extended, sea_levels_predicted, 'r')

    # -------- Second line of best fit (2000–2050) --------
    df_2000 = df[df['Year'] >= 2000]

    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    years_extended_2000 = np.arange(2000, 2051)

    sea_levels_predicted_2000 = result_2000.slope * years_extended_2000 + result_2000.intercept

    plt.plot(years_extended_2000, sea_levels_predicted_2000, 'g')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()