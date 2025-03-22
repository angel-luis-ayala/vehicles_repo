# vehicles_repo
# Proyecto: Análisis de vehículos

## Descripción
Esta  es una aplicación web interactiva en la que los usuarios pueden visualizar datos sobre vehículos en venta.

La aplicación proporciona un gráfico interactivo dependiendo la casilla que marque el usuario.

Si se marca la casilla del histograma la aplicación generará un gráfico interactivo sobre la distribución del kilometraje de los vehículos en venta.

Si se marca la casilla del gráfico de dispersión la aplicación generará un gráfico interactivo sobre la correlación entre el precio de los vehículos y su kilometraje.

Se utilizaron las siguientes librerías: pandas, streamlit y plotly.express.



Nota:
Se omitió el siguiente paso debido a que nuestros tutores mencionaron que hacerlo daría un error:

"Para hacer que Streamlit sea compatible con Render, añade un archivo de configuración de Streamlit al repositorio de tu proyecto en streamlit/config.toml con el siguiente contenido:
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
Le dirá a Render que busque en el sitio correcto para escuchar tu aplicación de Streamlit cuando la aloje en sus servidores."

URL de la aplicación en render:
https://vehicles-web-service.onrender.com