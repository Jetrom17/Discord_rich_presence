![](https://i.imgur.com/pRw7xVa.png)
> Fonte: [Pypresence](https://qwertyquerty.github.io/pypresence/html/index.html).

## Discord Rich Presence:

> O Rich Presence permite-lhe tirar partido da secção "Now Playing" totalmente renovada no perfil de um utilizador do Discord para ajudar as pessoas a jogar o seu jogo em conjunto. Os dados avançados do jogo - incluindo duração, pontuação, boss ou mapa atual e muito mais - vivem no Discord. Pode assistir ao jogo de um amigo diretamente a partir do popout do seu perfil, ou juntar-se através de belos embutidos de chat com informações em tempo real sobre as vagas abertas no grupo e o estado do jogo. Acabou-se a troca de nomes de utilizador e códigos de amigo, ou a dúvida se há espaço para ti. O Rich Presence é um convite vivo para jogar em conjunto ou para ver os seus amigos a darem cabo de si.

Fonte: https://discord.com/developers/docs/rich-presence/how-to

#

Ao contrário desse projeto, permite você personalizar seu perfil. Por exemplo, você pode fazer uma propaganda de algo ou simplesmente exibir o fuso horário local em tempo real, para os demais usuários próximos.

## Instalação:

```
git clone https://github.com/Jetrom17/Discord_rich_presence
cd Discord_rich_presence
pip install pypresence psutil pytz
python3 app.py
```

## Informações:

Definição do Fuso Horário:
```py
belem_timezone = pytz.timezone('America/Belem')
```
> Biblioteca pytz.

Definição do usuário:
```py
client_id = "00000000000000" # Substitua o ID do bot encontrado aqui: https://discord.com/developers/applications
RPC = Presence(client_id, pipe=0)
RPC.connect()
```

Definição do uso da sua CPU e RAM:

```py
cpu_usage = round(psutil.cpu_percent(), 1)
ram_usage = round(psutil.virtual_memory().percent, 1)
```
> Biblioteca psutil.

Definição do botão com url de destino:

```py
buttons = [
            {"label": "Sketchub", "url": "https://sketchub.in"},
        ]
```

Definição das imagens a serem exibidas:

```py
large_image="https://i.imgur.com/ncADWBT.jpeg",
small_image="https://i.imgur.com/pftnAO5.jpeg",
```

> Biblioteca pypresence.

> [!note]
> Há duas versões: `Python` e `Go`, estão na pasta `versions`.
