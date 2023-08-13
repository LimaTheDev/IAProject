import yfinance as yf

ticker = input("Digite o código da ação: ")
dados = yf.Ticker(ticker).history("2y")

treinamento = dados.reset_index()

#print(treinamento[["Date", "Close"]])

treinamento_date = treinamento["Date"].dt.date
treinamento = treinamento.rename(columns={"Date": "ds", "Close": "y"})

print(treinamento_date)
print(treinamento)
print(treinamento[["ds", "y"]])