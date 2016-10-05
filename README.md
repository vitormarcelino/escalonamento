# SISTEMAS OPERACIONAIS - ESCALONAMENTO DE PROCESSOS

## Como executar
Para execultar o programa na linha de comando Linux: `python algoritmos.py`

Ao executar o programa em Python, o usuário irá informar o número de processos, os tempos de entrada de cada processo, e o tempo de uso da cpu de cada processo. Após inserir esses dados, o usuário será questionado sobre qual algoritmo de escalonamento deseja simular a execução, são eles:

-FIFO
-SJF
-Round Robin (Preemptivo)
-EDF (Preemptivo)

Os algoritmos Preemptivos irão pedir ao usuário o quantum de processamento, e terão uma sobrecarga de preempção de 1 unidade de tempo. O algoritmo EDF, além de pedir o quantum ao usuário, irá pedir tambem as deadlines dos processos para a simulação da execução.
Os resultados que os algoritmos irão retornar, serãos os Turnaround Médio da execução.

## Exportar Gráfico Comparativo
Para exportar o gráfico comparativo o usuário irá inserir a opção 5 no menu de linha de comando, a partir disso o programa irá pedir o quantum e as deadlines e abrir o gráfico no navegador padrão do usuário.
O programa gerá um arquivo .JSON que servirar de entrada para o gráfico construido em JavaScript dentro do arquivo grafico.html.
Para contruir o gráfico foi utilizada a biblioteca Chart.js e jQuery.

## Licença
Copyright (c) 2016 Vitor Marcelino
Licensed under the MIT license.