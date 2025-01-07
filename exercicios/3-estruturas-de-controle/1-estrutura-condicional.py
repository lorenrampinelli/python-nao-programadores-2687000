# Declare 4 variáveis do tipo numérica
a = 1
b = 5
c = 2
d = 10

# Crie uma estrutura condicional para comparar dois números
if a < d:
  print(f"{a} e menor que {d}")
elif a > d:
  print(f"{a} e maior que {d}")
else:
  print(f"{a} e {b} sao iguais")

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor

if a < d:
  print(f"{d} e o maior numero")
else:
  print(f"{a} e o maior numero")
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor


# Insira outras condições na estrutura condicional usando o elif


# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"



# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if (d>a) and (d>b):
  print(f"{d} e maior que {a} e {b}!")
if c>a and c>b:
  print(f"{c} e maior que {a} e {c}")
if d>c or d<c:
  print(f"Apenas uma das duas condicoes e verdadeira")