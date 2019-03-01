#Repositório para o projeto de Inteligência Artificial#

### TITULO: Simulador de um agente em um ambiente variavel. ###

### SUMÁRIO DE VERSIONAMENTO ###
*Versão 1.0 26/02/19*
*Versão 1.1 01/03/19*

**Descrição Breve**
- v1.0:
	Foi criado a geração do mapa em interface gráfica utilizando a biblioteca do Canvas.
- v1.1:
	Criado as classes Elementos e Desenho e início da geração do mapa com a coloração dos elementos bem como suas posições.

**Descrição Detalhada**

===================================================================================================================
- v1.0:
	Foram criados dois arquivos.
	1. main.py
	2. diretório 'pacotes' contendo a classe Mapa.py


	O primeiro responsável pela chamada da classe Mapa e seus demais objetos, contendo todos os atributos responsáveis pela geração do gráfico.
	O Segundo contém todos os métodos responsáveis pela geração, população e atribuição de valores ao mapa em si.

===================================================================================================================
- v1.1:
	1. Classe **Elementos**:
		Contém todas as informações dos elementos do mapa (elemento, tamanho máximo, cor e pesos), retornando um objeto
	2. Classe **Desenho**:
		Contém todos os métodos que aplicam o 'desenho' à matriz gráfica. Posicionamento dos elementos, cores de cada elemento, interface de interação.

	A partir da criação das classes, deu-se início a aplicação do mapa com os elementos bem como suas posiçoes e colorações

===================================================================================================================

**Impacto**
- v1.0:
	Nenhum

- v1.1:
	Dependendo das alterações que são realizadas na classe Desenho, ela pode interferir nas outras classes, principalmente a Elementos
