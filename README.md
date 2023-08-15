# MoreLifeProjectt
Este projeto tem o intuito de ajudar pessoas que gostam de jogos competitivos, mas já tiveram problemas cardíacos, como princípio de infarto, a controlar o tempo que ficam no computador jogando, esses tipos de jogos que provocam o aumento dos batimentos cardiacos.

## Versão do python
- 3.11.3

## Bibliotecas utilizadas no projeto
- Kivy 2.2.0.dev0
- PySerial 3.5
- winotify

## Como Instalar o Kivy

Digite estes comandos no terminal

    py -m pip install --upgrade pip wheel setuptools
    py -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
    py -m pip install kivy.deps.gstreamer
    py -m pip install kivy.deps.angle
    pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/

###### OBS: Se o python da sua máquina não estiver no PATH, você terá que adicionar o python no PATH ou executar esses comandos diretamente na pasta onde está o "python.exe"

## Notas
Precisamos mudar a forma como o MoreLife está armazenando os dados locais o membro Andreas teva a ideia de mudar o arquivo db para json, pois ele acha q vai ser mais rápido e fácil de organizar as coisas ou colocar todos os dados locais para o FireBase como está o bando de login.
