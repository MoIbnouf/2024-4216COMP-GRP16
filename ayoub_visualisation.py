import pandas as pd
import matplotlib.pyplot as plt

def Ay_visualisation():
    # Load the data
    df = pd.read_csv('world-data-2023.csv')
    # Remove the dollar sign and commas from the 'GDP' and 'Co2-Emissions' columns, and convert them to float
    df['GDP'] = df['GDP'].str.replace(',', '').str.replace('$', '').astype(float)
    df['Co2-Emissions'] = df['Co2-Emissions'].str.replace(',', '').str.replace('$', '').astype(float)

    # Plot the correlation between GDP and Co2-Emissions
    plt.figure(1, figsize=(10, 5))
    plt.scatter(df["GDP"], df['Co2-Emissions'], alpha=0.6, edgecolors='w', color='blue')
    plt.title('Correlation between GDP and Co2-Emissions')
    plt.xlabel('GDP')
    plt.ylabel('Co2-Emissions')
    plt.show()

    # Get the 5 countries with the highest Co2-Emissions and plot
    top_co2_data = df.sort_values('Co2-Emissions', ascending=False).head(5)
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    plt.figure(1, figsize=(10, 5))
    co2_bars = plt.bar(top_co2_data['Country'], top_co2_data['Co2-Emissions'], color=colors, alpha=0.5)
    plt.legend(co2_bars, top_co2_data['Country'])
    plt.title('5 Countries with the highest Co2-Emissions')
    plt.xlabel('Country')
    plt.ylabel('Co2-Emissions')
    plt.show()

    # Get the 5 countries with the highest GDP and plot
    top_gdp_data = df.sort_values('GDP', ascending=False).head(5)
    plt.figure(1, figsize=(10, 5))
    gdp_bars = plt.bar(top_gdp_data['Country'], top_gdp_data['GDP'], color=colors, alpha=0.5)
    plt.legend(gdp_bars, top_gdp_data['Country'])
    plt.title('5 Countries with the highest GDP')
    plt.xlabel('Country')
    plt.ylabel('GDP')
    plt.show()


