import csv
import plotly.express as px
import pandas as pd
import pylab as plt
import seaborn as sns

def partie1() :

    data = pd.read_csv("seismes_2014.csv", delimiter=",")
    data.columns = ["instant", "lat", "lon", "pays", "mag", "profondeur"]

    total_seismes = len(data)
    print("Nombre total de séismes enregistrés en 2014 :", total_seismes)


    table_effectifs = data["pays"].value_counts().head(20)
    print("Table des effectifs des 20 lieux les plus fréquemment secoués dans le monde :")
    print(table_effectifs)

    noms = table_effectifs.index.tolist()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x="pays", y="mag", data=data[data["pays"].isin(noms)], whis=[0,100], order=noms)
    plt.xticks( rotation=90)
    plt.xlabel("Lieu")
    plt.ylabel("Magnitude")
    plt.title("Boîte à moustaches des 20 lieux les plus fréquemment secoués en 2014")



    top_6_lieux = data.groupby("pays")["mag"].max().nlargest(6)
    print("Les 6 lieux du monde qui enregistrent les plus fortes magnitudes :")
    print(top_6_lieux)

    # Nombre de séismes de magnitude inférieure ou égale à 2 en Californie
    californie_seismes = data[(data["pays"] == "California") & (data["mag"] <= 2)]
    nombre_seismes_californie = len(californie_seismes)
    print("Nombre de séismes de magnitude inférieure ou égale à 2 en Californie :", nombre_seismes_californie)

    # Nombre de séismes de magnitude inférieure ou égale à 2 en Alaska
    alaska_seismes = data[(data["pays"] == "Alaska") & (data["mag"] <= 2)]
    nombre_seismes_alaska = len(alaska_seismes)
    print("Nombre de séismes de magnitude inférieure ou égale à 2 en Alaska :", nombre_seismes_alaska)

    plt.show()

def partie_map_inf_5():
    # Définir le token Mapbox
    mapbox_token = 'pk.eyJ1Ijoic2hha3VuOSIsImEiOiJjbGljdWJ1ZjcwbWxiM3NtbzNyYWh1c3kzIn0.A8nMixa9JlGZUyY-YZaABg'

    # Charger les données depuis le fichier CSV
    data = pd.read_csv("seismes_2014.csv")

    # Filtrer les séismes de magnitude <5
    filtered_data = data[data['mag'] < 5]

    continuous_color_scale="rdgy"
    # Créer une carte de chaleur des séismes
    fig = px.density_mapbox(filtered_data, lat='lat', lon='lon', z='mag', radius=2,
                            center=dict(lat=0, lon=0), zoom=0,
                            mapbox_style='satellite', title='Carte de chaleur des séismes de magnitude inférieur a 5')
    fig.update_layout(mapbox=dict(accesstoken=mapbox_token))
    fig.show()

def partie_map_sup_5():
    # Définir le token Mapbox
    mapbox_token = 'pk.eyJ1Ijoic2hha3VuOSIsImEiOiJjbGljdWJ1ZjcwbWxiM3NtbzNyYWh1c3kzIn0.A8nMixa9JlGZUyY-YZaABg'

    # Charger les données depuis le fichier CSV
    data = pd.read_csv("seismes_2014.csv")

    # Définir la palette de couleurs
    palette = {
        3: 'hotpink',
        4: 'green',
        5: 'chocolate',
        6: 'blue',
        7: 'red',
        8: 'black'
    }
    # Filtrer les séismes de magnitude entre 3 et 9
    filtered_data = data[(data['mag'] > 5) & (data['mag'] <= 10)]
    mag = int(filtered_data['mag'].iloc[3])
    print(mag)
    print(filtered_data['mag'].iloc[3])
    print(filtered_data['mag'])
    # Créer une carte de chaleur des séismes
    fig = px.density_mapbox(filtered_data,lat='lat', lon='lon', z='mag', radius=10 + 10 * (mag - 5),
                            center=dict(lat=0, lon=0), zoom=0,
                            mapbox_style='streets', title='Carte de chaleur des séismes par rapport a leur magnitude entre 5 et 10',
                            color_continuous_scale=list(palette.values()))  # Utiliser la palette de couleurs

    fig.update_layout(mapbox=dict(accesstoken=mapbox_token))
    fig.show()


def partie3():
    mapbox_token = 'pk.eyJ1Ijoic2hha3VuOSIsImEiOiJjbGljdWJ1ZjcwbWxiM3NtbzNyYWh1c3kzIn0.A8nMixa9JlGZUyY-YZaABg'

    # Charger les données depuis le fichier CSV
    data = pd.read_csv("seismes_2014.csv")

    # Créer une carte circulaire des séismes
    fig = px.scatter_geo(data, lat='lat', lon='lon',
                        projection='natural earth',
                        title='Carte circulaire des séismes en fonction de leur magnitude',
                        color_continuous_scale='rdgy')

    fig.update_geos(showcountries=True, countrycolor="gray")
    fig.update_layout(geo=dict(showland=True, landcolor="lightgray"))

    fig.update_traces(marker=dict(size=5))
    fig.update_layout(mapbox=dict(accesstoken=mapbox_token))
    fig.show()