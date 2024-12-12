import time
import psutil
from pypresence import Presence

# Configuração inicial do cliente
client_id = "645734567432543587"  # Substitua pelo ID real
rpc = Presence(client_id)

try:
    rpc.connect()
except Exception as e:
    print("Erro ao conectar ao cliente RPC:", e)
    exit()

start_time = int(time.time())
print("Atualizando presença...")

try:
    while True:
        # Uso de CPU e RAM
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent

        # Configurando a presença
        try:
            rpc.update(
                state=f"CPU: {cpu_usage:.1f}%, RAM: {ram_usage:.1f}%",
                details="Sabedoria diária, que transforma sua vida!",
                start=start_time,
                large_image="https://i.imgur.com/aHOM9Tk.png",
                large_text=f"Uso de CPU: {cpu_usage:.1f}%",
                small_text=f"Uso de RAM: {ram_usage:.1f}%",
                buttons=[
                    {
                        "label": "Método Destiny",
                        "url": "https://proverb-day.pages.dev/",
                    }
                ]
            )
        except Exception as e:
            print("Erro ao atualizar a presença:", e)

        time.sleep(5)  # Atualiza a cada 5 segundos

        if time.time() - start_time >= 24 * 3600:
            break
except KeyboardInterrupt:
    print("Encerrando o programa.")
finally:
    rpc.close()
