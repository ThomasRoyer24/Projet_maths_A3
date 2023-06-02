library(shiny)
library(threejs)
tab_color <- c("#8EFFC3","#78FF60","#A9FF47","#F4FF28","#FF900A","#F44900","#EA1B0","#000000")
app <- shinyApp(
    ui = bootstrapPage(
        globeOutput('plot')
    ),
    server = function(input, output) {
        # Lecture du fichier CSV
        data <- read.csv("seismes_2014.csv")

        latitude <- data[data$mag > 2, 2]
        longitude <- data[data$mag > 2, 3]
        mag <- as.integer(na.omit(data[data$mag > 2, 5]))
        profondeur <- data[ , 6]
        index_non_na <- !is.na(data[data$mag > 2, 5])
        latitude_sans_na <- latitude[index_non_na]
        longitude_sans_na <- longitude[index_non_na]


        output$plot <- renderGlobe({
            globejs(
                lat = c(NA, latitude_sans_na),
                long = c(NA, longitude_sans_na),
                pointsize = 0.5,
                color = tab_color[mag],
                atmosphere = FALSE,
                bg = "black",
                value = profondeur / 4
            )
        })
    }
)

runApp(app, launch.browser = TRUE)