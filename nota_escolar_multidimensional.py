__author__ = 'bruno'

"""
    Este programa recebe uma lista multidimensional de 3 dimensoes
    e que cada sub-lista e representada ppor um estudante e suas 4
    notas. O programa oferece as operacoes de exibir os dados como
    notas dos alunos. Exibir a maior e a menor nota de cada aluno 
    e a funcao average que calcula a media final de cada aluno
"""

# esta funcao a penas imprime as notas dos alunos
def printGrades(grades):
    students = len(grades) # numero de estudantes
    
    # como eu sei que o numero de provas é o mesmo para cada row
    # posso utilizar exams para armazenar o numero de elementos 
    # para uma futura iteração
    exams = len(grades[0]) # numero de exames
    
    print("The list is:")
    for i in range(exams):
        print("[%d]" % i)
    print()
    
    # iteração sobre o aluno
    for i in range(students):
        print("grades[%d]" % i)
        
        for j in range(exams):
            print(grades[i][j])
            
        print()

# esta funcao imprime a menor nota dos 3 alunos
def minimum(grades):
    lowscore = 100
    
    for studentsExams in grades:
        for score in studentsExams:
            if score < lowscore:
                lowscore = score
    return lowscore

# esta funcao imprime a maior nota dos 3 alunos
def maximum(grades):
    highscore = 0
    
    for studentsExams in grades:
        for score in studentsExams:
            if score > highscore:
                highscore = score
                
    return highscore

# esta funcao imprime a media para cada aluno
def average(setOfGrades):
    total = 0.0
    
    # como estou iterando a penas uma vez tenho que
    # passar somente o row
    for grade in setOfGrades:
        total += grade
        
    return total / len(setOfGrades)

# programa principal

grades = [[77, 68, 86, 73],
          [96, 87, 89, 91],
          [70, 90, 86, 81],
          ]

printGrades(grades)
print("The lowest grade is", minimum(grades))
print("The highest grade is", maximum(grades))

# imprime a media de cada aluno 
for i in range(len(grades)):
    print("The average of student",i,"is:",average(grades[i]))