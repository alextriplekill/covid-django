import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
import os

BASE_DIR = dir_path = os.path.dirname(os.path.realpath(__file__))
BASE_NAME = "table.html"
path_infected = os.path.join(BASE_DIR, 'graphData\\time_series_covid19_confirmed_global.csv')
path_recovered = os.path.join(BASE_DIR, 'graphData\\time_series_covid19_recovered_global.csv')
path_deaths = os.path.join(BASE_DIR, 'graphData\\time_series_covid19_deaths_global.csv')
path_html = os.path.join(BASE_DIR, 'table.html')

# Create your views here.

arr_confirm = pd.read_csv(path_infected, sep=',', header=0)
arr_confirm.drop(columns=['Lat','Long'], inplace=True)
arr_confirm.fillna('', inplace=True)
arr_confirm["Infected"] = arr_confirm.iloc[:,-1]
arr_confirm['Location'] = arr_confirm['Country/Region'] + " " + arr_confirm['Province/State']
arr_confirm.drop(columns=['Country/Region','Province/State'], inplace=True)
arr_confirm.drop(list(arr_confirm.filter(regex=r'(\d+/\d+/\d+)')), axis=1, inplace=True)
arr_recover = pd.read_csv(path_recovered, sep=',', header=0)
arr_recover.drop(columns=['Lat', 'Long', 'Province/State'], inplace=True)
arr_confirm["Recovered"] = arr_recover.iloc[:, -1].round()
arr_deaths = pd.read_csv(path_deaths, sep=',', header=0)
arr_deaths.drop(columns=['Lat', 'Long', 'Province/State'], inplace=True)
arr_confirm["Deaths"] = arr_deaths.iloc[:, -1]
arr_confirm.set_index('Location', inplace=True)
file = open(BASE_NAME, "wb")

data = arr_confirm.to_html().encode('utf-8')
file.write(data)
file.close()
webbrowser.open(path_html)
#plot = arr_confirm.plot(kind="barh")
#plot.show()
