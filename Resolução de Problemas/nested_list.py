'''
O Problema: Listas Aninhadas (Nested Lists)

Dada a identificação de cada aluno em uma turma de N estudantes e sua respectiva nota, armazene esses dados em uma lista aninhada (uma lista dentro de outra) e imprima o nome(s) de qualquer aluno(s) que tenha(m) a segunda menor nota.
Regras importantes:

    A Segunda Menor Nota: Se houver um ou mais alunos com a nota mais baixa de todas, ignore-os. Você quer encontrar quem está exatamente no "segundo degrau" de baixo para cima.

    Empates: Se houver múltiplos alunos com essa mesma "segunda menor nota", você deve listar os nomes de todos eles.

    Ordem de Exibição: Se houver mais de um aluno na segunda menor nota, imprima os nomes em ordem alfabética, um em cada linha.

Exemplo de Entrada:

Imagine que você recebeu os seguintes dados:

    Chi, nota 20

    Alpha, nota 50

    Beta, nota 50

Exemplo de Saída:

    A menor nota é 20.

    A segunda menor nota é 50.

    Como Alpha e Beta têm nota 50, e "Alpha" vem antes de "Beta" no dicionário, a saída seria:
'''

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        aluno = [name, score]
        records.append(aluno)
        
        cont = len(records)
        records_ordem =sorted(records)
    
    for i in range(cont):
        name = records_ordem[i][0]
        print(f'{name}')
  


   


