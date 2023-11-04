x = int(input('Informe a quantidade de alunos na turma: '))
for i in range(1, x+1, +1):
  print(f'{i}° Aluno')
  for j in range(i):
    num1 = int(input('Informe a primeira nota: '))
    num2 = int(input('Informe a segunda nota: '))
    num3 = int(input('Informe a terceira nota: '))
    media = (num1+num2+num3)/3
    print(f'A média é: {media:.2f}')
    if media > 6:
      print('Aluno aprovado!')
      break
    else:
      print('Aluno reprovado!')
      break