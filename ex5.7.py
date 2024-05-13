def contagemRegressiva(n):
    if n == 0:
        print("Contagem regressiva finalizada!")
        return
    print(n)
    contagemRegressiva(n - 1)
    
contagemRegressiva(5)