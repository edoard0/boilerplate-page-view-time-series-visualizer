import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df=pd.read_csv("fcc-forum-pageviews.csv",parse_dates=True,index_col="date")

# Clean data
df = df[(df["value"]>=df["value"].quantile(0.025)) & (df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,7))

    plt.plot(df,c="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_grouped=pd.DataFrame(df_bar.groupby([df_bar.index.year,df_bar.index.month])["value"].mean()).reset_index(level=1)

    df_grouped.columns=['Months', 'value']

    df_final=df_grouped.pivot(columns='Months', values='value')
    df_final.columns=["January","February","March","April","May","June","July","August","September","October","November","December"]

    # Draw bar plot
    plot=df_final.plot.bar(xlabel="Years",ylabel="Average Page Views",figsize=(15,7))
    fig = plot.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box.columns=['date', 'Page Views', 'Year', 'Month']
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True,figsize=(15,7))
    sns.boxplot(data=df_box,x="Year",y="Page Views", ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box,x="Month",y="Page Views", ax=ax2,order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
