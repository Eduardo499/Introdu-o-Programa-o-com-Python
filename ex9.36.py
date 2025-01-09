import os

def calcular_espaco(diretorio):
    if not os.path.exists(diretorio) or not os.path.isdir(diretorio):
        print(f"O diretório '{diretorio}' não existe ou não é válido.")
        return

    def calcular_tamanho_dir(diretorio):
        tamanho_total = 0
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                tamanho_total += os.path.getsize(caminho_completo)
        return tamanho_total

    diretorios_info = []
    for raiz, dirs, _ in os.walk(diretorio):
        tamanho_dir = calcular_tamanho_dir(raiz)
        diretorios_info.append((raiz, tamanho_dir))

    if not diretorios_info:
        print("Nenhum diretório encontrado no diretório informado.")
        return

    html_content = """<html>
<head>
    <title>Espaço Ocupado por Diretórios</title>
</head>
<body>
    <h1>Espaço Ocupado por Diretórios e Subdiretórios</h1>
    <table border="1">
        <tr>
            <th>Nome do Diretório</th>
            <th>Tamanho (bytes)</th>
        </tr>
"""
    for caminho, tamanho in diretorios_info:
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

    arquivo_saida = os.path.join(diretorio, "espaco_diretorios.html")
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Página HTML gerada com sucesso: {arquivo_saida}")

if __name__ == "__main__":
    diretorio = input("Digite o caminho do diretório: ").strip()
    calcular_espaco(diretorio)
