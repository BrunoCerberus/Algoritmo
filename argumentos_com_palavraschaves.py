"""
	Existe uma outra maneira bem legal de trabalhar com argumentos padroes de funcoes
	Quando vc define argumentos padroes, ao inserir valores a eles vc tera de obedece a sequencia em que
	a funcao foi definida. Vc pode inserir argumento em qualquer sequencia usando palavras-chaves mais  o valor
"""
# nesta funcao eu defino tres argumentos padroes, url, Flash e CGI
# note que name nao e um argumento padrao, omitir um valor para ele sera considerado um erro de compilacao
def gerar_webSite(name, url = "www.deitel.com", Flash = "nao", CGI = "sim"):
	print("Gerando site pedido pelo",name,"usando a url",url)

	if Flash == "sim":
		print("Flash esta ativado")
	if CGI == "sim":
		print("Scripts CGI's estao ativados")
	print("") # apenas pula uma linha


gerar_webSite("Deitel")

# note que aqui pela definicao da funcao, o paramero url vem antes que Flash, digitando explicitamente o nome dos paramentros e
# os valores de seus argumentos, voce nao precisara obedecer uma sequencia

gerar_webSite("Deitel", Flash = "sim", url = "www.deitel.com/new")

# nao precisa ter um argumento padrao para acessar o parametro por meio de palavras-chaves
# a unica obrigacao, ja que name nao tem um argumento padrao, e que name tem ao menos um valor
gerar_webSite(CGI = "nao", name = "Bruno")


# gerar_webSite(CGI="nao",Flash="sim") # claramente essa linha de código gerará um erro
	
