import random
import time

#Criação da função insertionSort
def insertionSort(A):
	#O loop for começa no segundo elemento (indice 1) até o último elemento da string porque consideramos que o primeiro elemento está ordenado 
	for j in range(1, len(A)):
		#para cada elemento da string armazena em lista
		lista = A[j]
		#A variável i inicia na possição anterior à j (porque iniciamos na segunda posição)
		i = j-1
		#enquanto o primeira posição for maior ou igual a zero e o valor dessa possição for maior que o valor da lista
		while i >= 0 and A[i] > lista: 
			#o valor da possição é copiado para a posição seguinte (guarda em cima do valor mais baixo mas esse valor está na lista)
			A[i+1] = A[i]
			#voltamos a possição um passo para trás (atenção se o i for 0 estiver na primeira posição após o decremento fica a -1)
			i = i-1
		#copiamos o valor que estava guardano na lista (o que perdeu o valor) para o primeiro lugar da comparação, posição do i antes do while
		A[i+1] = lista
	return A

#Criação da função bubbleSort
def bubbleSort(A):
	#contagem do comprimento da lista
	x = len(A)
	# corre todos os indices até ao final que é x
	for i in range(x):
		# o valor de j começa com 0 e vai até ao penúltimo
		for j in range(0, x - i - 1):
			# verifica se o valor da posição do array onde está é maior que a próxima possição do mesmo array
			if A[j] > A[j + 1]:
				# troca as posições do array um pelo outro
				A[j], A[j + 1] = A[j + 1], A[j]
	return A

#Criação da função mergeSort
def mergeSort(A):
	# Verifica se a lista possui mais que um elemento, se tiver um elemento a lista encontra-se ordenada
	if len(A) > 1:
		#  Divide a lista (array) em duas partes iguais
		metade = len(A) // 2
		# A primeira metade coloca na variável A_esq (esquerda)
		A_esq = A[:metade]
		# A outra metade coloca na variável A_dir (direita)
		A_dir = A[metade:]
		# É novamente chamada a função mas só corre a A_esq, entra no ciclo if de novo até ficar com 1 elemento 
		mergeSort(A_esq)
		# Exatamente o mesmo mas com a parte direita
		mergeSort(A_dir)
		# criação das variáveis i, j e t com o valor de 0 para cada uma delas
		i = j = t = 0
		# Aqui verifica a existência das duas listas, verificando o valor de cada variável (i e j) sendo inferior a cada uma das partes
		while i < len(A_esq) and j < len(A_dir):
			# Aqui verifica se qual a parte menor
			if A_esq[i] < A_dir[j]:
				# aqui vai guardar o valor da parte esquerda na posição t da variável A
				A[t] = A_esq[i]
				# aqui incrementamos a variável i
				i += 1
			else:
				# aqui guardamos a parte direita na posição t da variável A
				A[t] = A_dir[j]
				# incrementamos a variável j
				j += 1
			# incrementamos a variável t
			t += 1
		# Aqui verifica a existência da lista da esquerda (A_esq)
		while i < len(A_esq):
			# guarda a parte da esquerda na posição t da variável A
			A[t] = A_esq[i]
			# incrementa a variável i
			i += 1
			# incrementa a variável t
			t += 1
		# Aqui verifica a existência da lista da direita (A_dir)
		while j < len(A_dir):
			# guarda a parte direita na posição t da variável A
			A[t] = A_dir[j]
			# incrementa a variável j
			j += 1
			# incrementa a variável t
			t += 1
	return A, tempo

# Criação da função Quick Sort
def quickSort(A):
	# Verificação se a lista tem mais que 1 elemento
	if len(A) <= 1:
		return A
	else:
		# Atribuição do pivot ao primeiro elemento da lista
		pivo = A[0]
		# colocação dos numeros menores que pivot para menos
		menos = [i for i in A[1:] if i <= pivo]
		# colocação dos numeros maiores que pivot para mais
		mais = [i for i in A[1:] if i > pivo]
		# o pivot é adicionado à lista de saída e o return faz voltar a repetir a função para os menores do pivot e outra repetição dos maiores
		# por cada vez que qualquer das listas reenicia o pivot fica na sua posição correcta
		# por cada vez que reeniciar a função é adicionado um pivot na posição correcta
		# quando acabar é retornado a lista total dos pivo ordenados
		return quickSort(menos) + [pivo] + quickSort(mais)

#criação da lista aleatória
def ale(tmin, tmax, vmin, vmax):
	t = random.randint(tmin, tmax)
	return [random.randint(vmin, vmax) for _ in range(t)]

# Quadro de tamanhos:
# tamanho mínimo do array
tmin = 1
# tamanho máximo do array
tmax = 20
# valor mínimo de cada elemento
vmin = -100
# valor máximo de cada elemento
vmax = 100

sep = "--------------------------------------------------------"
sep2 = "########################################################"

# Juntar a lista aleatória com o tempo num único array
def juntaListaTempo(li,tp):
	li_str=str(li)
	tp_str=str(tp)
	st=li_str+tp_str
	return st

def contaInsertionSort(l1):
        #Início da contagem do tempo
        inicio=time.time()
        #Irá executar a função Quick Sort
        l1=bubbleSort(l1)
        #retorno da string completa para fora da função e a informação do tempo de execução também
        fim = time.time()
        tempo = fim - inicio
        return l1, tempo

def contaBubbleSort(l2):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l2=bubbleSort(l2)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l2, tempo

def contaMergeSort(l3):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l3=quickSort(l3)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l3, tempo

def contaQuickSort(l4):
	#Início da contagem do tempo
	inicio=time.time()
	#Irá executar a função Quick Sort
	l4=quickSort(l4)
	#retorno da string completa para fora da função e a informação do tempo de execução também
	fim = time.time()
	tempo = fim - inicio
	return l4, tempo

l1tempm=l2tempm=l3tempm=l4tempm=10
l1tempmx=l2tempmx=l3tempmx=l4tempmx=l1total=l2total=l3total=l4total=0

# Apresentação na tela os resultados
for i in range (200):
	# Este conjunto vai gerar aleatóriamente uma lista e coloca para cada l esta mesma lista (l1, l2, l3 e l4)
	lale = ale(tmin, tmax, vmin, vmax)
	l1 = l2 = l3 = l4 = lale

	print ("\n")
	print (sep2)
	print ("Lista inicial aleatória:\n",lale,)
	print (sep2)
	print ("\n")
	print ("Lista inicial para p método Insertion Sort:\n",l1)
	l1=contaInsertionSort(l1)
	l1l=l1[0]
	l1t=l1[1]
	print ("Lista l1: ",l1l) #####
	print ("Tempo l1: ",l1t) #####
	#Esta condição vai calcular o minimo e máximo do Insertion Sort
	if l1t < l1tempm:
		l1listam = l1l
		l1tempm = l1t
	if l1t > l1tempmx:
		l1listax = l1l
		l1tempmx = l1t
	print ("Lista ordenada pelo método Insertion Sort:\n",l1l)
	print ("O tempo que executa o método Insertion Sort:\n", l1t)
	print (sep)
	print ("Lista inicial para o método Bubble Sort: ",l2)
	l2=contaBubbleSort(l2)
	l2l=l2[0]
	l2t=l2[1]
	print ("Lista l2: ",l2l) #####
	print ("Tempo l2: ",l2t) #####
	#Esta condição vai calcular o minimo e máximo do Bubble Sort
	if l2t < l2tempm:
		l2listam = l2l
		l2tempm = l2t
	if l2t > l2tempmx:
		l2listax = l2l
		l2tempmx = l2t
	print ("Lista ordenada pelo método Bubble Sort:\n",l2l)
	print ("O tempo que executa o método Bubble Sort:\n",l2t)
	print (sep)
	print ("Lista inicial para o método Merge Sort: ",l3)
	l3=contaMergeSort(l3)
	l3l=l3[0]
	l3t=l3[1]
	#Esta condição vai calcular o minimo e máximo do Merge Sort
	if l3t < l3tempm:
		l3listam = l3l
		l3tempm = l3t
	if l3t > l3tempmx:
		l3listax = l3l
		l3tempmx = l3t
	print ("Lista ordenada pelo método Merge Sort:\n",l3l)
	print ("O tempo que executa o método Merge Sort:\n",l3t)
	print (sep)
	print ("Lista inicial para o método Quick Sort: ",l4)
	l4=contaQuickSort(l4)
	l4l=l4[0]
	l4t=l4[1]
	#Esta condição vai calcular o minimo e máximo do Quick Sort
	if l4t < l4tempm:
		l4listam = l4l
		l4tempm = l4t
	if l4t > l4tempmx:
		l4listax = l4l
		l4tempmx = l4t
	print ("Lista ordenada pelo método Quick Sort:\n",l4l)
	print ("O tempo que executa o método Quick Sort:\n",l4t)
	print (sep)
	#Somatório para a média
	l1total=l1total+l1t
	l2total=l2total+l2t
	l3total=l3total+l3t
	l4total=l4total+l4t

#Divisão para a média
l1total=l1total/200
l2total=l2total/200
l3total=l3total/200
l4total=l4total/200

#Cálculo das médias por métodos
print ("\n")
print (sep2)
print ("O tempo mais curto do método Insertion Sort foi de ",l1tempm," com a lista ",l1listam,".")
print ("A média do método Insertion Sort é de :",l1total," segundos.")
print ("O tempo que levou mais pelo método Insertion Sort foi de ",l1tempmx," com a lista ",l1listax,".")
print (sep2)
print ("O tempo mais curto do método Bubble Sort foi de ",l2tempm," com a lista ",l2listam,".")
print ("A média do método Bubble Sort é de :",l2total," segundos.")
print ("O tempo que levou mais tempo pelo método Bubble Sort foi de ",l2tempmx," com a lista ",l2listax,".")
print (sep2)
print ("O tempo mais curto do método Merge Sort foi de ",l3tempm," com a lista ",l3listam,".")
print ("A média do método Merge Sort é de :",l3total," segundos.")
print ("O tempo que levou mais tempo pelo método Merge Sort foi de ",l3tempmx," com a lista ",l3listax,".")
print (sep2)
print ("O tempo mais curto do método Quick Sort foi de ",l4tempm," com a lista ",l4listam,".")
print ("A média do método Quick Sort é de :",l4total," segundos.")
print ("O tempo que levou mais tempo pelo método Quick Sort foi de ",l4tempmx," com a lista ",l4listax,".")
