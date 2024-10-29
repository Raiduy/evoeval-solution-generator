import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('90_data.csv')

def plot_boxplots(df, column, ylabel, filename):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Run Name', y=column, data=df)
    plt.title(f'{column} Boxplot Grouped by Algorithm')
    plt.ylabel(ylabel)
    plt.xlabel('Algorithm')
    plt.savefig(filename, format='png', dpi=300)
    # plt.show()

plot_boxplots(df, 'PKG (uJ)', 'PKG Energy Consumption (uJ)', './figures/90_cpu.png')

plot_boxplots(df, 'DRAM (uJ)', 'DRAM Energy Consumption (uJ)', './figures/90_dram.png')
