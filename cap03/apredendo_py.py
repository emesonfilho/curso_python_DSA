print("========== CALCULADORA EM PYTHON ==========")
while True:
	opcoes = print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")

	processo = int(input("Qual operação deseja executar? "))

	numero_1 = float(input("Primeiro número:"))
	numero_2 = float(input("Segundo número:"))

	if processo == 1:
		print(f"A soma dos dois números inseridos é igual a {numero_1 + numero_2}")
	elif processo == 2:
		print(f"A subtração dos dois números inseridos é igual a {numero_1 - numero_2}")
	elif processo == 3:
		print(f"A multiplicação dos dois números inseridos é igual a {numero_1 * numero_2}")
	elif processo == 4:
		print(f"A divisão dos dois números inseridos é igual a {numero_1 / numero_2}")
	else:
		print("Nenhuma opção válida foi inserida.")

	print()
	print("Deseja fazer mais alguma operação?\n1. Sim\n2. Não")
	#print("1. Sim\n2. Não")

	decisao = int(input(""))

	if decisao == 2:
		break

	print("==="*30)
print(">>>>>>>>>>>>>> FIM DO PROGRAMA <<<<<<<<<<<<<<")
input()