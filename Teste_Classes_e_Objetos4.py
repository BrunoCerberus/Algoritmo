# importando a classe
from Classes_e_Objetos4 import Time

# Inicializando o objeto (instanciando)
relogio = Time()

# Exibindo a hora inicial nos doi padroes
print("O horario militar inicial e:", relogio.printMilitary())
print("O horario convencional inicial e:", relogio.printStandard())

# mudar as horas do relogio
relogio.setTime(13, 27, 6)
print("-"*10)

# Exibindo novamente as horas nos dois padroes
print("O horario militar depois de setTime() e:", relogio.printMilitary())
print("O horario convencional depois de setTime() e:", relogio.printStandard())

# configurando um novo horario pelos metodos de acesso
relogio.setHour(4)
relogio.setMinute(3)
relogio.setSecond(34)
print('-'*10)

# Exibindo o horario novo nos dois padroes novamente
print("O horario militar depois dos metodos acessores e:", relogio.printMilitary())
print("O horario convencional depois dos metodos acessores e:", relogio.printStandard())

