# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from itertools import cycle #IMPORTA LISTA CIRCULA PARA O ALGORITMO ROUND ROBIN

#FUNÇÃO DO ALGORITMO FIFO
def fifo ():
	entradas = tmpEnt
	tempos = tmpExe
	for j in range(0,n):
		for i in range(0,n-1):
			if entradas[i]>entradas[i+1]:
				Aux = entradas[i+1] #ORDENA A CHEGADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux
				Aux = tempos[i+1] #ORDENA AS OS TEMPOS COM BASE NA CHEGADA
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
	soma = 0
	relogio = 0
	for x in xrange(0,n):
		relogio += tempos[x] #INCREMENTA O RELOGIO COM O TEMPO DE EXECUÇÃO DO PROCESSO
		soma += relogio - entradas[x] #INCREMENTA A SOMA COM O TEMPO FINAL DO PROCESSO (RELOGIO) - O TEMPO DE ENTRADA
		pass
	return float(soma/n);

#FUNÇÃO DO ALGORITMO SJF
def sjf ():
	entradas = tmpEnt
	tempos = tmpExe
	for j in range(0,n):
		for i in range(0,n-1):
			if tempos[i]>tempos[i+1]:
				Aux = tempos[i+1] #ORDENA AS OS TEMPOS COM BASE NA CHEGADA
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
				Aux = entradas[i+1] #ORDENA A CHEGADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux	
	print entradas
	print tempos
	soma = 0
	relogio = 0
	for x in xrange(0,n):
		relogio += tempos[x] #INCREMENTA O RELOGIO COM O TEMPO DE EXECUÇÃO DO PROCESSO
		soma += relogio - entradas[x] #INCREMENTA A SOMA COM O TEMPO FINAL DO PROCESSO (RELOGIO) - O TEMPO DE ENTRADA
		pass
	return float(soma/n);


#FUNÇÃO DO ALGORITMO ROUND ROBIN
def rr ():
	entradas = list(tmpEnt) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(tmpExe) # MESMA IDEIA DE CIMA
	relogio = 0
	processados = [0]*n
	count = 0
	soma = 0
	for processo, entrada in cycle(zip(tempos, entradas)): #LISTA CIRCULAR
		#print processo, " - ", entrada, " - ", count, " - ", processados[count]
		if processo > processados[count]: ## AINDA FALTA SER PROCESSADO
			if (processo-processados[count] > quantum) and (entrada <= relogio):
				processados[count]+=quantum
				relogio+=quantum
				print "Processo ", count+1, " está em processamento. R=", relogio
			elif (processo-processados[count] <= quantum) and (entrada <= relogio):
				aux = processo-processados[count]
				processados[count]+=aux
				relogio+=aux
				print "Processo ", count+1, " está em seu último processamento. R=", relogio
				soma+=relogio-entrada
			else: 
				print "Processo ", count+1, " não chegou ainda."
		else:
			print "Processo ", count+1, " está pronto."
		if count==n-1:
			count=0
		else:
			count+=1
		if processados == tempos:
			break
	print processados
	return float(soma/n)

#FUNÇÃO DO ALGORITMO EDF
def edf():
	entradas = list(tmpEnt) #COPIA A LISTA DE ENTRADAS PARA UMA NOVA LISTA, QUE SERÁ ORDENADA
	tempos = list(tmpExe) # MESMA IDEIA DE CIMA
	for j in range(0,len(deadlines)):
		for i in range(0,len(deadlines)-1):
			if deadlines[i]>deadlines[i+1]:
				Aux = deadlines[i+1] #ORDENA AS DEADLINES
				deadlines[i+1] = deadlines[i]
				deadlines[i] = Aux
				Aux = entradas[i+1] #ORDENA A CHEGADA COM BASE NA DEADLINE
				entradas[i+1] = entradas[i]
				entradas[i] = Aux 
				Aux = tempos[i+1] #ORDENA A O TEMPO COM BASE NA DEADLINE
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
	soma = 0
	for x in xrange(0,n):
		aux = tempos[x] - entradas[x]	#TEMPO DE EXECUÇÃO - TEMPO DE ENTRADA
		soma += (n-x)*aux					#MULTIPLICA
		pass
	return float(soma/n);

#LEITURA DAS DEADLINES
def lerDeadlines():
	del deadlines[:]
	for x in xrange(0,n):
		print "Informe a Deadline do processo ", x, ": "
		deadlines.append(input())
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