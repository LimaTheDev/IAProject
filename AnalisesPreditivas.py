import yfinance as yf

ticker = input("Digite o código da ação: ")
dados = yf.Ticker(ticker).history("2y")

treinamento = dados.reset_index()
treinamento["ds"] = treinamento["Date"].dt.date
treinamento = treinamento.rename(columns={"Close": "y"})

print(treinamento[["ds", "y"]])