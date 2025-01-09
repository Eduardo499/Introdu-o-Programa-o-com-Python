filmes={
"drama": ["Cidadão Kane","O Poderoso Chefão"],
"comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
"policial": ["Chuva Negra","Desejo de Matar","Difícil de Matar"],
"guerra": ["Rambo","Platoon","Tora!Tora!Tora!"]
}

página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<p>%s</p>" % e)

página.write("""
</body>
</html>
""")
página.close()
