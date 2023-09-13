import io
import base64
from flask import Flask, render_template, request
import pandas as pd
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from keras.models import load_model
import pickle

# crear instancia para la aplicacion
app = Flask(__name__)

# funcion para crear grafico
def create_plot(predicted_stock_price_future, ticker):
  plt.plot(predicted_stock_price_future, color='green')
  plt.title(f'Predicción de tendencia acciones de {ticker}')
  plt.xlabel('Fecha (días)')
  plt.ylabel(f'Precio de la Acción de {ticker}')
  plt.legend()  
  # guardar el gráfico en un búfer
  buffer = io.BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)       
  # codificar el gráfico en una cadena base64
  plot_data = base64.b64encode(buffer.read()).decode()     
  return plot_data

# funcion base
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    ticker = request.form['ticker']
    start_date = request.form['start_date']
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = request.form['end_date']
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    # funcion obtener datos de entrenamiento
    def get_data2(ticker):
      try:
        tickerData = yf.Ticker(ticker)
        stock_data = tickerData.history(period='1d', start=start_date, end=end_date) 
      except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))
      return stock_data
    # aplicar funcion para extraer los datos
    data = get_data2(ticker)
    # obtener precios de cierre
    prices = data['Close'].values.reshape(-1, 1)
    # normalizar los datos
    scaler = MinMaxScaler(feature_range=(0, 1))
    prices_scaled = scaler.fit_transform(prices)
    # funcion para crear secuencias 
    def create_sequences(data, seq_length):
      sequences = []
      for i in range(len(data) - seq_length):
        seq = data[i:i+seq_length]
        target = data[i+seq_length]
        sequences.append((seq, target))
      return sequences    
    # establecer secuencia - aplicar funcion
    seq_length = 15
    data_seq = create_sequences(prices_scaled, seq_length)
    data_seq = np.array([seq for seq, target in data_seq])
    # cargar el modelo pre-entrenado
    model = load_model('RNN_model.h5')
    # establecer input para el rango de dias a predecir
    days_to_predict = int(request.form['days_to_predict'])
    # obtener las predicciones para los próximos 30 días
    # recortar las secuencias de entrada para que tengan una longitud fija (=seq_length)
    data_seq = data_seq[-days_to_predict:]  
    # obtener las predicciones para los próximos 'days_to_predict' días
    predicted_stock_price_future = model.predict(data_seq)
    predicted_stock_price_future = scaler.inverse_transform(predicted_stock_price_future)
    predicted_stock_price_future = np.squeeze(predicted_stock_price_future)
    # aplicar funcion crear grafico   
    plot_data = create_plot(predicted_stock_price_future, ticker)

    return render_template('index.html', plot_data=plot_data)
   
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
