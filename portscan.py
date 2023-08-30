import socket #  fornece funcionalidades para criar, manipular e gerenciar sockets

ports = [21,22,80,443,445,3306,25] # Essa lista contém os números das portas que o programa irá verificar quanto à abertura.  

for port in ports: # loop que percorre cada número de porta na lista ports
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # um novo objeto de socket é criado usando a família de endereços da Internet (AF_INET) e o tipo de socket de fluxo (SOCK_STREAM). Isso cria um socket TCP/IP
	client.settimeout(0.1) # Define um tempo limite (timeout) de 0.1 segundos para a conexão
	code = client.connect_ex(("nome do host ou IP", port)) # aqui o socket tenta se conectar ao endereço, 'port' é a porta sendo verificada e a função 'connect_ex' retorna um código de erro. Se o código for 0, isso significa que a conexão foi estabelecida com sucesso.
	if code == 0: # Essa parte verifica se a conexão foi estabelecida com sucesso e, nesse caso, imprime a porta e a mensagem "OPEN", indicando que a porta está aberta.
		print(port, "OPEN")
