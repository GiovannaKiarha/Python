Criar uma função no Python, de forma inicial, sempre será definido por def e o nome da sua função em seguida.

Lembre-se que além de você, outras pessoas vão ler o código. Então, crie a sua função com um nome de fácil reconhecimento. 

Neste exercício, o que foi pedido era criar uma função que realiza-se um cálculo simples de expoente, mas que no momento que o usuário não passasse um número para o expoente, utiliza-se como default o número 2.

1º Passo:
Crie a sua função e dê os parâmetros que serão utilizados nela.
Neste caso, quis utilizar o nome potencia para que outras pessoas pudessem ler e já entender de cara sobre o que era a função. E para parâmetros (coisas que serão utilizadas na função), eu coloquei o nome de base e expoente para fácil entendimento.

2º Passo:
Precisamos armazenar essas parâmetros em variáveis. Lembrando que no Python, para criar uma variável, você só precisar dar o nome da variável e colocar o = (igual). No caso, como é com interação do usuário, preciso que ele digite e para isso, utilizo o input. Além disso, como estamos trabalhando com números, precisamos definir que é um intenger.

Observação: Se reparar, na variável de expoente, não utilizamos o int pois teremos um default armazenado caso a pessoa não defina um número e caso coloca-se como int, o programa poderia reconhecer como 0 e era algo que não queríamos.

3º Passo:
Lembra que existe a chance da pessoa não passar um valor para o expoente? É por isso que teremos que utilizar o if/else.

Utilizamos o if para mostrar no console o resultado puxando o print. Utilizamos uma f string para poder ler a resposta puxando a função e os parâmetros definidos pela pessoa. 
Como existem duas possibilidades, utilizamos apenas o if e o else, sem a necessidade de um elif. Quando utilizamos o else, é apenas a única outra alternativa do que pode acontecer e que definimos para acontecer. Tudo na programação somos NÓS que definimos. No segundo caso, como é algo default (no caso, o número 2), não precisamos definir o segundo parâmetro e por isso, só puxamos a variável armazenada da base.
