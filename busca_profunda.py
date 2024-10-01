arvore = {
    'belo horizonte': ['araraquara', 'são carlos', 'três lagoas', 'são paulo'],
    'araraquara': ['ribeirão preto', 'são carlos'],
    'ribeirão preto': ['araraquara', 'são paulo', 'campo grande'],
    'campo grande': ['ribeirão preto', 'três lagoas'],
    'são paulo': ['belo horizonte', 'três lagoas', 'campinas'],
    'são carlos': ['belo horizonte', 'três lagoas', 'campinas', 'araraquara', 'ribeirão preto', 'campo grande'],
    'três lagoas': ['belo horizonte', 'são paulo', 'campo grande', 'são carlos'],
    'campinas': ['são paulo', 'são carlos']
}

def busca_profundidade(arvore, comeco, objetivo):
    visitados = set()  
    pilha = [(comeco, [comeco])]  

    while pilha:
        cidade_atual, caminho = pilha.pop()  

        if cidade_atual == objetivo:
            return caminho 

        if cidade_atual not in visitados:
            visitados.add(cidade_atual)  

           
            for vizinho in arvore.get(cidade_atual, []):
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))  

    return None  


resultado = busca_profundidade(arvore, 'belo horizonte', 'campo grande')
print(resultado)
