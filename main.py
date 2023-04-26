import os

import pandas as pd
import re
from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

ROOT_DIR = os.path.dirname(os.path.abspath(path="plotting"))
from funcs.common_fun import cleanse, plot_line, plot_scatter, plot_bar, plot_pie_chart, plot_area, plot_boxa, \
    plot_histo, plot_hexbina, plot_barh

app = FastAPI()


@app.post("/plot_line")
def plot_line_graph(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    print(df2.dtypes)
    plot_line(df2.head(10), xaxis, yaxis)


@app.post("/plot_pie_chart")
def plot_pchart(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_pie_chart(df2.head(10), xaxis, yaxis)


@app.post("/plot_area")
def plot_areap(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_area(df2.head(10), xaxis, yaxis)


@app.post("/plot_box")
def plot_box(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_boxa(df2.head(10), xaxis, yaxis)


@app.post("/plot_hist")
def plot_hist(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_histo(df2.head(10), xaxis, yaxis)


@app.post("/plot_hexbin")
def plot_hexbin(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_hexbina(df2.head(10), xaxis, yaxis)


@app.post("/plot_scatter")
def plot_scatter_graph(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_scatter(df2.head(10), xaxis, yaxis)


@app.post("/plot_bar")
def plot_bar_graph(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_bar(df2.head(10), xaxis, yaxis)


@app.post("/plot_barh")
def plot_bar_graph_h(xaxis, yaxis):
    df = pd.read_csv("file_resource/readfile.csv")
    df2 = cleanse(df)
    plot_barh(df2.head(10), xaxis, yaxis)


@app.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"file_resource/readfile.csv"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
