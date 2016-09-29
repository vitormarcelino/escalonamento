# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from itertools import cycle #IMPORTA LISTA CIRCULA PARA O ALGORITMO ROUND ROBIN

#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	lista = ordena(0) #ORDENA A LISTA POR ORDEM DE CHEGADA
	soma = 0
	for x in xrange(0,n):
		aux = lista[x][1] - lista[x][0]		#TEMPO DE EXECUÇÃO - TEMPO DE ENTRADA
		soma += (n-x)*aux					#MULTIPLICA
		pass
	return float(soma/n);

#FUNÇÃO DO ALGORITMO SJF
def sjf ():
	lista = ordena(1) #ORDENA A LISTA POR TEMPO DO PROCESSO
	soma = 0
	for x in xrange(0,n):
		aux = lista[x][1] - lista[x][0]		#TEMPO DE EXECUÇÃO - TEMPO DE ENTRADA
		soma += (n-x)*aux					#MULTIPLICA
		pass
	return float(soma/n);

#FUNÇÃO DO ALGORITMO ROUND ROBIN
def rr ():
	lista = ordena(0) #ORDENA A LISTA POR CHEGADA
	lista = cycle(lista)
	relogio = 0
	for processo in lista: #LISTA CIRCULAR 
		if (processo[0]<=relogio & processo[1]>=quantum):
			processo[1]-=quantum
		elif (processo[0]<=relogio & processo[1]<quantum):
			processo[1]-=processo[1]
			next
		relogio +=quantum
		print(processo)
		if(relogio>50):
			break
	return 0

#FUNÇÃO DO ALGORITMO EDF
def edf():
	for j in range(0,len(deadlines)):
		for i in range(0,len(deadlines)-1):
			if deadlines[i]>deadlines[i+1]:
				Aux = deadlines[i+1] #ORDENA AS DEADLINES
				deadlines[i+1] = deadlines[i]
				deadlines[i] = Aux
				Aux = tmpEnt[i+1] #ORDENA A CHEGADA COM BASE NA DEADLINE
				tmpEnt[i+1] = tmpEnt[i]
				tmpEnt[i] = Aux 
				Aux = tmpExe[i+1] #ORDENA A O TEMPO COM BASE NA DEADLINE
				tmpExe[i+1] = tmpExe[i]
				tmpExe[i] = Aux
	soma = 0
	for x in xrange(0,n):
		aux = tmpExe[x] - tmpEnt[x]	#TEMPO DE EXECUÇÃO - TEMPO DE ENTRADA
		soma += (n-x)*aux					#MULTIPLICA
		pass
	return float(soma/n);

#LEITURA DAS DEADLINES
def lerDeadlines():
	for x in xrange(0,n):
		deadlines.append(input("Informe a Deadline do processo "))
		pass
	


#ORDENAÇÃO PASSANDO O TIPO: 0 = ORDENAÇÃO POR CHEGADA, 1 = ORDENAÇÃO POR TEMPO DE PROCESSO
def ordena (tipo):
	lista = zip(tmpEnt, tmpExe)
	lista.sort(key=lambda x: x[tipo])
	return lista

#LÊ A QUANTIDADE DE PROCESSOS E CRIA AS LISTAS DE TEMPO DE EXECUÇÃO E TEMPO DE ENTRADA PARA CADA PROCESSO
n = int(input ("Informe o numero de processos: "))
tmpExe = []
tmpEnt = []
deadlines = []

#LÊ OS TEMPOS DE EXECUÇÃO E DE ENTRADA PARA CADA PROCESSO
for x in xrange(1,n+1):
	print "Tempo de entrada do processo ", x, ": "
	tmpEnt.append(float(input()))
	print "Tempo de execução do processo ", x, ": "
	tmpExe.append(float(input()))

#SOLICITA AO USUARIO QUE INFORME O ALGORITMO DE ESCALONAMENTO DESEJADO
print "Selecione o algoritmo de escalonamento\n (1) FIFO\n (2) SJF\n (3) Round Robin\n (4) EDF \n (0) Sair"
cmd = input ("Escolha: ")

#ENQUANDO A ESCOLHA FOR DIFERENTE DE 0, EXECUTA O RESPECTIVO ALGORITMO, OU RETORNA COMANDO INVALIDO
while cmd != 0:
	if cmd == 1:
		print "============ FIFO ============"
		print "TURNAROUND MEDIO: ", fifo()
		print "=============================="
		pass
	elif cmd == 2:
		print "============ SJF ============="
		print "TURNAROUND MEDIO: ", sjf()
		print "=============================="
		pass
	elif cmd == 3:
		quantum = float(input("Insira o valor do quantum: "))
		print "========= ROUND ROBIN ========"
		print "TURNAROUND MEDIO: ", rr()
		print "=============================="
		pass
	elif cmd == 4:
		lerDeadlines()
		print "============ EDF ============="
		print "TURNAROUND MEDIO: ", edf()
		print "=============================="
		pass
	else:
		print "Comando Inválido"
		pass
	cmd = input ("Escolha outro comando: ")