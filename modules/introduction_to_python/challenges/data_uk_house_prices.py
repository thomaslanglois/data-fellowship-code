import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.models import HoverTool
from bokeh.plotting import output_file, show
from bokeh.palettes import Dark2_5 as palette
from bokeh.models import NumeralTickFormatter, Panel
from bokeh.layouts import column
from bokeh.models.widgets import Tabs
import itertools

if __name__ == "__main__":
    """ load raw data """
    df = pd.read_excel('./datasets/UK House price index-v2.xls', sheet_name='Average price')

    """ clean the data """
    """ drop NaT indexes and columns with NaN values """
    df = df.loc[df.index.dropna()].dropna(axis=1)
    """ convert index values to datetime """
    df.index = pd.to_datetime(df.index)

    print('df.shape: {}'.format(df.shape))
    print('df.head(5): {}'.format(df[list(df.columns.values)[:5]].head(5)))

    """ find top n borrows which have increased the most over the whole period """
    n_top_borrows = 30
    top_borrows = df.loc[[df.index.min(), df.index.max()]].pct_change().dropna() \
        .transpose() \
        .sort_values('2018-12-01', ascending=False) \
        .head(n_top_borrows).index.values

    """ plot average gross prices history for top borrows """
    p1 = figure(title='UK House Prices top {} gainers'.format(n_top_borrows), plot_width=1200, plot_height=800, x_axis_type='datetime')
    p1.yaxis[0].formatter = NumeralTickFormatter(format='0,0.0')

    colors = itertools.cycle(palette)

    for borrow, c in zip(top_borrows, colors):
        dates = df.index.values
        avg_price = df[borrow].values
        pline = p1.line(x=dates, y=avg_price, color=c, line_width=1, legend=borrow)
        p1.add_tools(HoverTool(renderers=[pline],
                               tooltips=[('date', '@x{%Y-%m-%d}'), ('borrow', borrow), ('avg_price', '£@y{0,0.00}')],
                               formatters={'x': 'datetime'},
                               mode='vline'))

    p1.legend.location = 'top_left'
    p1.legend.click_policy = 'hide'
    p1.legend.label_text_font_size = '5pt'
    p1.legend.background_fill_alpha = 0.5
    p1.legend.spacing = 0
    p1.legend.padding = 0
    p1.legend.margin = 0

    layout1 = column([p1])
    tab1 = Panel(child=layout1, title='UK House Average Price - Top Gainers')

    """ plot average percentage price change history for top borrows """
    cum_pct_ret_df = (df.diff().dropna().cumsum()/df.iloc[0])*100

    p2 = figure(title='UK House Prices top {} gainers'.format(n_top_borrows), plot_width=1200, plot_height=800, x_axis_type='datetime')
    p2.legend.location = 'top_left'
    p2.yaxis[0].formatter = NumeralTickFormatter(format='0.0')
    colors = itertools.cycle(palette)

    for borrow, c in zip(top_borrows, colors):
        dates = cum_pct_ret_df.index.values
        avg_price = cum_pct_ret_df[borrow].values
        pline = p2.line(x=dates, y=avg_price, color=c, line_width=1, legend=borrow)
        p2.add_tools(HoverTool(renderers=[pline],
                               tooltips=[('date', '@x{%Y-%m-%d}'), ('borrow', borrow), ('avg_price', '@y{0,0.00}%')],
                               formatters={'x': 'datetime'},
                               mode='vline'))

    p2.legend.location = 'top_left'
    p2.legend.click_policy = 'hide'
    p2.legend.label_text_font_size = '5pt'
    p2.legend.background_fill_alpha = 0.5
    p2.legend.spacing = 0
    p2.legend.padding = 0
    p2.legend.margin = 0

    layout2 = column([p2])
    tab2 = Panel(child=layout2, title='UK House Average Percentage Price Change - Top Gainers')

    """ display all tabs """
    tabs = Tabs(tabs=[tab1, tab2])
    show(tabs)

    # use pd.melt to turn a df columns in one observation per cell


