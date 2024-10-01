arvore = {
    'belo horizonte': ['araraquara', 'são carlos', 'três lagoas', 'são paulo'],
    'araraquara': ['ribeirão Preto', 'são carlos'],
    'ribeirão preto': ['araraquara', 'são paulo', ' campo grande'],
    'campo grande':['ribeirão preto', 'três lagoas'],
    'são paulo': ['belo horizonte', 'três lagoas', 'campinas'],
    'são carlos': ['belo horizonte', 'três lagoas', 'campinas', 'araraquara', 'ribeirão preto', 'campo grande'],
    'três lagoas': ['belo horizonte', 'são paulo', 'campo grande', 'são carlos'],
    'campinas': ['são paulo', 'são carlos']

}

def busca_largura(arvore, comeco, objetivo):
    visitados = []  
    fila = [(comeco, [comeco])]  

    while fila:
        fila_atual, caminho = fila.pop(0) 

        if fila_atual == objetivo:
            return caminho  
        if fila_atual not in visitados:
            visitados.append(fila_atual)  

            
            for vizinho in arvore.get(fila_atual, []):
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho])) 

    return None  

resultado = busca_largura(arvore, 'belo horizonte', 'campo grande')
print(resultado)



