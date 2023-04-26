import matplotlib.pyplot as plt
from fastapi import FastAPI, File, UploadFile


def cleanse(df):
    col_list = df.columns
    for col in col_list:
        if df[col].dtype == float:
            df[col] = df[col].fillna(0.0)
            if (df[col] % 1 == 0).all():
                df[col] = df[col].astype(int)
    return df


def plot_line(df, x_axis, y_axis):
    df.plot(kind='line',

            x=x_axis,
            y=y_axis, )
    plt.title("line graph")
    plt.show()


def plot_bar(df, x_axis, y_axis):
    df.plot(kind='bar',

            x=x_axis,
            y=y_axis)
    plt.title("bar graph")
    plt.show()


def plot_scatter(df, x_axis, y_axis):
    df.plot(kind='scatter',

            x=x_axis,
            y=y_axis)

    plt.title("scatter graph")
    plt.show()


def plot_pie_chart(df, x_axis, y_axis):
    df.plot(kind='pie',
            x=x_axis,
            y=y_axis)
    plt.title("Pie chart")
    plt.show()


def plot_area(df, x_axis, y_axis):
    df.plot(kind='area',
            x=x_axis,
            y=y_axis)
    plt.title("area chart")
    plt.show()


def plot_histo(df, x_axis, y_axis):
    df.plot(kind='hist',
            x=x_axis,
            y=y_axis)
    plt.title("area chart")
    plt.show()


def plot_boxa(df, x_axis, y_axis):
    df.plot(kind='box',
            x=x_axis,
            y=y_axis)
    plt.title("box chart")
    plt.show()


def plot_barh(df, x_axis, y_axis):
    df.plot(kind='barh',
            x=x_axis,
            y=y_axis)
    plt.title("barh")
    plt.show()


def plot_hexbina(df, x_axis, y_axis):
    df.plot(kind='hexbin',
            x=x_axis,
            y=y_axis)
    plt.title("hexbin")
    plt.show()
