from prophet import Prophet
from prophet.plot import plot_plotly
import plotly_express as px
from AnalisesPreditivas import treinamento


modelo = Prophet()

modelo.fit(treinamento)

periodo = modelo.make_future_dataframe(periods=90)

previsoes = modelo.predict(periodo)

previsoes.tail()

plot_plotly(modelo, previsoes)