import csv
import plotly.express as px
import pandas as pd

def partie1() :
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer l'en-tête du fichier CSV

    for row in reader:
        line_count += 1



    # Exemple d'utilisation
    csv_file = 'data.csv'  # Remplacez 'data.csv' par le chemin vers votre fichier CSV
    line_count = count_lines(csv_file)
    print(f"Nombre de lignes dans le fichier CSV : {line_count}")


    def count_countries(csv_file):
        country_counts = {}

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Ignorer l'en-tête du fichier CSV

            for row in reader:
                country = row[3]  # Indice 3 correspondant à la colonne du pays
                if country in country_counts:
                    country_counts[country] += 1
                else:
                    country_counts[country] = 1

        return country_counts

    # Exemple d'utilisation
    csv_file = 'seismes_2014.csv'  # Remplacez 'data.csv' par le chemin vers votre fichier CSV
    result = count_countries(csv_file)

    for country, count in result.items():
        print(f"{country}: {count}")

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