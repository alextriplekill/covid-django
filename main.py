import pandas as pd
import webbrowser
import requests
import matplotlib.pyplot as plt
import os
import constants

BASE_DIR = dir_path = os.path.dirname(os.path.realpath(__file__))
BASE_NAME = "table.html"
path_infected = os.path.join(BASE_DIR, 'graphData\\confirmed.csv')
path_recovered = os.path.join(BASE_DIR, 'graphData\\recovered.csv')
path_deaths = os.path.join(BASE_DIR, 'graphData\\deaths.csv')
path_html = os.path.join(BASE_DIR, 'table.html')

def updateData():
    confirmed = requests.get(constants.TOTAL_CASES_URL)
    with open(path_infected, 'wb') as f:
        f.write(confirmed.content)
    recovered = requests.get(constants.RECOVERED_URL)
    with open(path_recovered, 'wb') as f:
        f.write(recovered.content)
    deaths = requests.get(constants.DEATHS_URL)
    with open(path_deaths, 'wb') as f:
        f.write(deaths.content)
# Create your views here.
updateData()
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
