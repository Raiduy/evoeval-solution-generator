import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('4_data.csv')

def plot_boxplots(df, column, ylabel):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Label', y=column, data=df)
    plt.title(f'{column} Boxplot Grouped by Algorithm')
    plt.ylabel(ylabel)
    plt.xlabel('Algorithm')
    plt.show()

plot_boxplots(df, 'PKG (uJ)', 'PKG Energy Consumption (uJ)')

plot_boxplots(df, 'DRAM (uJ)', 'DRAM Energy Consumption (uJ)')
