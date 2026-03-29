# 📦 Criador de Automações
Projeto desenvolvido para facilitar a criação de automações (Realizar ações no PC) tais como abrir um aplicativo, controlar mouse e teclado, tirar print da tela entre outras funcionalidades de uma forma de interpretação de texto, facilitando o manuseio do mesmo.

## 📜 Como usar
O codigo consiste em ler e interpretar de uma forma considerada correta para o modulo de leitura, que é baseada em Python. Abaixo terá uma lista de todas as palavras reservadas e seus devidos parametros:

`sleep(segundos)` - Tem a mesma funcionalidade do time.sleep() no Python. No lugar de "segundos" coloque o valor que desejar, lembrando que no momento so suporta valores INT.
`click(x, y)` - Função responsavel por clicar em algum local com o mouse, posição baseada em Pixels da tela (x, y). No lugar do "x" coloque a largura em Pixels e no "y" altura em Pixels.
`PressR(botao)` - Função responsavel por clicar e soltar (simulação de apertar) um botão do teclado. No lugar de "botao" coloque um botão do seu teclado, exemplo: PressR(A).
`PressH(botao, tempo_segurando)` - Função responsavel por clicar e segurar uma tecla por determinado tempo em segundos. No lugar de "botao" coloque a tecla desejada e no lugar de "tempo_segurando" coloque o tempo de pressão dessa tecla.
`Write(texto)` - Função responsavel por digitar algum conjunto de caracteres em seguida (texto, paragrafo etc...). No lugar de "texto" coloque o texto que desejar.

Vale ressaltar que o modulo suporta o uso de # para comentar uma linha dentro do arquivo de texto lido.

**Exemplo de arquivo:**
```
# EXEMPLO DE COMENTARIO
Click(10, 500)
sleep(1)
Write(Olá, mundo)
PressR(enter)
```

## 📋 Sobre o projeto
Estar em constante desenvolvimento, inclusive planejo criar um interface em Flet para este projeto, pois seria mais agil ainda criar automações rapidas, principalmente para usuarios comuns de computadores. Qualquer FeedBack é bem-vindo, se puder deixe já sua ideia!