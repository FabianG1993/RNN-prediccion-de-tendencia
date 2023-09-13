# RNN-prediccion-de-tendencia
Red neuronal recurrente para la predicción de tendencia de diferentes activos financieros. 

## En qué consiste el modelo

1. **Carga de Datos**: Se crea una funcion para extraer los datos sobre los precios de los activos a traves de la libreria especializada yfinance. 

2. **Procesamiento de Datos**: Una vez se obtienen los datos, se procesa la información y se prepara para el entrenamiento. 

3. **Predicción**: Se entrena un red neuronal recurrente con capas LSTM para la predicción de tendencia. 

4. **Evaluación del modelo**: Se aplica la métrica accuracy (número de predicciones correctas dividido por el número total de predicciones) para la evaluación del modelo. Se obtuvo un score de 0.83. 

5. **Guadar modelo**: Se guarda el modelo en formato .h5 para posteriomente llevarlo a nuestra aplicación web. 

## En qué consiste la interfaz 

1. **Estructura**: La interfaz consiste en tres archivos basicamente: un archivo index.html (esquema de la aplicación web), styles.css (formas, estilos, colores de la interfaz) y app.py (codigo python usando el framework Flask)

2. **App**: La aplicación se basa en el framework Flask de python. Basicamente la aplicación toma los datos ingresados para hacer la predicción. Luego, muestra los resultados a través de un grafico en donde se observa la tendencia del activo correspondiente.

## Cómo Utilizar    

1. Ingresar los datos.
2. Haz clic en el botón "Hacer prediccion".
3. La aplicación procesará los datos y mostrará un grafico de linea con la tendencia del activo para el # de días establecidos. 

## Requisitos del Sistema

- Python en su versión más reciente. 
- Navegador web moderno (Chrome, Edge, Mozilla Firefox, Safari, etc.).

## Uso Local (Opcional)

Si deseas ejecutar la aplicación localmente, puedes seguir estos pasos:

1. Clona este repositorio en tu ordenador.
2. Asegúrate de tener Python instalado y las bibliotecas necesarias.
3. Abre el archivo .ipynb en un entorno Jupyter Notebook.
4. Ejecuta las celdas para cargar y guardar el modelo.
5. Ejecuta el archivo app.py y ve al terminal.
5. Inicia el servidor local y accede a la aplicación a través de tu navegador.

## Notas

- Este proyecto tiene fines informativos y/o educativos. Los resultados pueden variar y no deben utilizarse como base única para tomar decisiones importantes.

## Créditos

- Autor: Fabián García Gómez
- Contacto: datasolu7ion@gmail.com
