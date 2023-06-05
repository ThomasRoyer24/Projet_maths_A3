import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

# Charger les données depuis le fichier CSV
data = pd.read_csv("10yearsOfHugeSismicActivity.csv", delimiter=",")

data.columns = ["time", "latitude", "longitude", "depth", "mag", "magType", "nst", "gap", "dmin", "rms",
                "net", "id", "updated", "place", "type", "horizontalError", "depthError", "magError",
                "magNst", "status", "locationSource", "magSource"]

# pour affichier le graph d'un seul pays !!! changer les noms de variable
#data_californie = data[data["pays"] == "California"]
#data_californie_mag = data_californie[data_californie["mag"] >= 3]

# visualisation des seismes dont la distance est inférieure à 60km       1 -> 120km
data_dmin = data[data["dmin"] <= 0.5]

print(data.size)

corr, _ = pearsonr(data_dmin["depth"].to_numpy(), data_dmin["mag"].to_numpy())
print(corr)


#affichier la corelation entre la profondeur et la magnitude
#cov = correlation(data_dmin["depth"].to_numpy(), data_dmin["mag"].to_numpy())
#print(cov)


# Créer le graphique de dispersion
plt.scatter(data_dmin["depth"], data_dmin["mag"])

# Ajouter les étiquettes des axes
plt.xlabel("Profondeur")
plt.ylabel("Magnitude")

# Afficher le graphique
plt.show()