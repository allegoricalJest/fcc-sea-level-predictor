import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    lineBF1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    xBF1 = range(df["Year"].min(), 2051)
    yBF1 = (xBF1 * lineBF1.slope) + lineBF1.intercept

    plt.plot(xBF1, yBF1)

    # Create second line of best fit
    df_2k = df[df["Year"] >= 2000]

    lineBF2 = linregress(df_2k["Year"], df_2k["CSIRO Adjusted Sea Level"])
    xBF2 = range(2000, 2051)
    yBF2 = (xBF2 * lineBF2.slope) + lineBF2.intercept

    plt.plot(xBF2, yBF2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()