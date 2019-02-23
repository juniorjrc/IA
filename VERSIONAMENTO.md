# PADRÃO DE DOCUMENTAÇÃO 

O Projeto contem uma branch master e uma branch para cada usuário.

A Branch master é onde está o projeto com alterações validadas, ou seja, foi desenvolvido aquilo
que se esperava em aula e validado pelo próprio professor. Portanto o projeto que estiver na Branch master
é o que está em sua forma mais atualizada.

A Branch de cada usuário é de responsabilidade unica, ou seja, cada usuário é responsavel pela própria branch.
Caso alguém deseja alterar o código que está na master, ou deseja apresentar alguma melhoria, deve seguir os passos abaixo:

- 1 Passo
  - Clonar a master em seu computador. 
- 2 Passo
  - Realizar a alteração e analise de impacto no projeto. 
- 3 Passo
  - Descrever a alteração e possiveis impactos no arquivo README na qual sofrerá o commit. 
- 4 Passo
  - Realizar o pull na SUA branch e avisar os demais desenvolvedores para a analise de alteração. 


Conforme descrito no passo 3, será necessário documentar a alteração no README. A fim de padronizarmos isso,
foi criado um modelo, portanto o seu README deve seguir o modelo descrito na sessão Abaixo.
#### obs:   
Caso não saiba como gerenciar o versionamento, leia o artigo:
https://fjorgemota.com/versionamento-semantico-ou-como-versionar-software/


## EXEMPLO README
Repositório para o projeto de Inteligência Artificial

TITULO: Simulador de um agente em um ambiente variavel.


###### SUMÁRIO DE VERSIONAMENTO ######

- Vesão 1.0 (coloque o numero da sua versão aqui)
	
	- Descrição Breve (descreva rapidamente o que foi feito)
	###### Criação dos Objetos Mapa, Elementos, Desenhista. ###### 
	
	- Descrição Detalhada (descreva detalhadamente o que foi trabalhado nas classes citadas acima)
	###### O objeto mapa é responsável por manter as informações de mapa e abstrair o processo na geração do mapa. ######
	###### O Desenhista é responsável por desenhar na matriz do mapa(não é o mapa que desenha em si mesmo, mas o desenhista). ######
	###### Os Elementos são conjuntos de dados armazenados em um dicionario, na qual todo tipo de Terreno é descrito lá e atribuido um peso. ######
	
	- Impacto (descreva as Classes e métodos que sofrerão impactos)
	###### Nenhum ######
	
	


