from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument

# Sostituisci questi valori con le tue credenziali API di Telegram
api_id =
api_hash = ""
channel_username = ""  # Inserisci l'username o ID del canale

# Inizializza il client
client = TelegramClient("telegram_scan", api_id, api_hash)

async def get_total_size():
    total_size = 0
    count = 0

    async with client:
        async for message in client.iter_messages(channel_username):
            if message.file:
                total_size += message.media.document.size  # Somma la dimensione del file
                count += 1

    print(f"Numero totale di file: {count}")
    print(f"Dimensione totale: {total_size / (1024 * 1024 * 1024):.2f} GB")

# Avvia lo script
with client:
    client.loop.run_until_complete(get_total_size())
