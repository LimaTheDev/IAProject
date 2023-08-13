import yfinance as yf

ticker = input("Digite o código da ação: ")
dados = yf.Ticker(ticker).history("2y")

treinamento = dados.reset_index()

print(treinamento[["Date", "Close"]])

treinamento["Date"] = treinamento["Date"].dt.date

print(treinamento["Date"])
print(treinamento)
