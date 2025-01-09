import os

def gerar_pagina_arquivos(diretorio):
    if not os.path.exists(diretorio) or not os.path.isdir(diretorio):
        print(f"O diretório '{diretorio}' não existe ou não é válido.")
        return

    arquivos_info = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            tamanho = os.path.getsize(caminho_completo)
            arquivos_info.append((caminho_completo, tamanho))

    if not arquivos_info:
        print("Nenhum arquivo encontrado no diretório.")
        return

    html_content = """<html>
<head>
    <title>Lista de Arquivos</title>
</head>
<body>
    <h1>Arquivos no Diretório</h1>
    <table border="1">
        <tr>
            <th>Nome do Arquivo</th>
            <th>Tamanho (bytes)</th>
        </tr>
"""
    for caminho, tamanho in arquivos_info:
        caminho_relativo = os.path.relpath(caminho, diretorio)
        html_content += f"""
        <tr>
            <td>{caminho_relativo}</td>
            <td>{tamanho}</td>
        </tr>
"""
    html_content += """
    </table>
</body>
</html>
"""

    arquivo_saida = os.path.join(diretorio, "arquivos.html")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Página HTML gerada com sucesso: {arquivo_saida}")

if __name__ == "__main__":
    diretorio = input("Digite o caminho do diretório: ").strip()
    gerar_pagina_arquivos(diretorio)
