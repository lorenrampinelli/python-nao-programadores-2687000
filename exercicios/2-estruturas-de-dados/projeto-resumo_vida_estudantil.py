# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante_1 = {}

estudante_1['nome'] = input("Digite seu nome: ")
estudante_1['ano_LinkedIn'] = int(input("Qual ano voce comecou a estudar no LinkedIn Learning? "))
estudante_1['ano_atual'] = int(input("Em qual ano estamos? "))
cursos = input("Por favor, digite os cursos que estudou no LinkedIn Learning, separados por virgula, em ordem cronológica: ")
estudante_1['cursos'] = cursos.split(', ')

# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante_1['ano_atual'] - estudante_1['ano_LinkedIn']
total_cursos = len(estudante_1['cursos'])
primeiro_curso = estudante_1['cursos'][0]
ultimo_curso = estudante_1['cursos'][-1]
print(f"{estudante_1['nome']} comecou a estudar no LinkedIn Learning em {estudante_1['ano_LinkedIn']}. Desde entao, ja sao {total_anos} anos de estudos e um total de {total_cursos} cursos realizados. O primeiro curso foi {primeiro_curso} e o mais recente e {ultimo_curso}.")
