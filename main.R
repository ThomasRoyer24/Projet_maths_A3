library(leaflet)

# Créer une carte de base
map <- leaflet()

# Ajouter des tuiles de fond (fond de carte)
map <- addTiles(map)

# Exemple de données de points avec différentes couleurs
points <- data.frame(
  lon = c(-73.9683, -74.0059, -71.0589),
  lat = c(40.7851, 40.7128, 42.3601),
  couleur = c("red", "green", "blue")
)

# Ajouter les points à la carte avec des couleurs différentes
map <- addCircleMarkers(map, data = points, lng = ~lon, lat = ~lat, color = ~couleur)

# Afficher la carte
map
