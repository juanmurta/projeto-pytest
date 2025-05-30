# sistema gerencial

# calcular o gaturamento
def calcular_faturamento():
    vendas = [1000, 2000, 3000, 4000, 5000]
    faturamento = sum(vendas)
    return faturamento


# calcular o custo
def calcular_custo(cotacao_dolar):
    custo = 1000 * cotacao_dolar
    return custo


# calcular o lucro
def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro