import os

def gerar_pagina_html(diretorio):
    if not os.path.exists(diretorio) or not os.path.isdir(diretorio):
        print(f"O diretório '{diretorio}' não existe ou não é válido.")
        return
    
    arquivos = []
    for raiz, _, arquivos_nomes in os.walk(diretorio):
        for nome in arquivos_nomes:
            if nome.lower().endswith(('.jpg', '.png')):
                arquivos.append(os.path.join(raiz, nome))
    
    if not arquivos:
        print("Nenhum arquivo JPG ou PNG encontrado no diretório.")
        return
    
    html_content = "<html>\n<head>\n<title>Lista de Imagens</title>\n</head>\n<body>\n"
    html_content += "<h1>Imagens Encontradas</h1>\n<ul>\n"
    for arquivo in arquivos:
        caminho_relativo = os.path.relpath(arquivo, diretorio)
        html_content += f'<li><a href="{caminho_relativo}" target="_blank">{caminho_relativo}</a></li>\n'
    html_content += "</ul>\n</body>\n</html>"
    
    arquivo_saida = os.path.join(diretorio, "imagens.html")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Página HTML gerada com sucesso: {arquivo_saida}")

if __name__ == "__main__":
    diretorio = input("Digite o diretório para buscar imagens: ").strip()
    gerar_pagina_html(diretorio)