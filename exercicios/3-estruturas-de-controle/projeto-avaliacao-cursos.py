# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, 
# caso verdadeiro deverá imprimir na tela essa informação, 
# além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ['Python', 'Java', 'Excel', 'Logica de Programacao', 'SQL']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_python = 'Python'
curso_java = 'Java'
curso_excel = 'Excel'


# 3. Crie um dicionário vazio para armazenar a nota do curso
notas_curso = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso_python in cursos:
  print(f"{curso_python} esta na lista de cursos")
  notas_curso[curso_python]=int(input(f"Qual nota vc da para o curso {curso_python} (de 0 a 5)?"))
if curso_java in cursos:
  print(f"{curso_java} esta na lista de cursos")
  notas_curso[curso_java] = int(input(f"Qual nota vc da para o curso {curso_java} (de 0 a 5)?"))
if curso_excel in cursos:
  print(f"{curso_excel} esta na lista de cursos")
  notas_curso[curso_excel] = int(input(f"Qual nota vc da para o curso {curso_excel} (de 0 a 5)?"))
else:
  print("Infelizmente este curso nao se encontra na lista")
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

print(notas_curso)