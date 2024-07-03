# pip install pypresence psutil pytz

from pypresence import Presence
import psutil
import time
import datetime
import pytz

# Timezone
belem_timezone = pytz.timezone('America/Belem')

client_id = "0000000000000"  # ID do bot (substitua pelo ID real)
RPC = Presence(client_id, pipe=0) 
RPC.connect()  # Inicia o loop de handshake

def update_presence():
    start = time.time()

    while True:
        # Atualize a hora atual em Belém
        current_time = datetime.datetime.now(belem_timezone)
        formatted_time = current_time.strftime('%I:%M %p')

        # Uso de CPU e RAM
        cpu_usage = round(psutil.cpu_percent(), 1)
        ram_usage = round(psutil.virtual_memory().percent, 1)

        buttons = [
            {"label": "Sketchub", "url": "https://sketchub.in"},
        ]

        RPC.update(
            state=f"CPU: {cpu_usage}%, RAM: {ram_usage}%",
            details=f"Horário de Belém: {formatted_time}",
            large_image="https://i.imgur.com/ncADWBT.jpeg",
            small_image="https://i.imgur.com/pftnAO5.jpeg", 
            start=start,
            buttons=buttons,
            large_text=f"Uso de CPU: {cpu_usage}%",
            small_text=f"Uso de RAM: {ram_usage}%"
        )

        time.sleep(3)  # Atualiza a cada 3 segundos

        # 86400 s - 24 h (um dia)
        if time.time() - start >= 86400:
            break

update_presence()
