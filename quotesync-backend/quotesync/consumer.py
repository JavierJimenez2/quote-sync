# quotesync/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class QuoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Añadir al grupo de 'quotes'
        await self.channel_layer.group_add("quotes", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Eliminar del grupo de 'quotes'
        await self.channel_layer.group_discard("quotes", self.channel_name)

    # Método para enviar mensaje cuando haya cambios
    async def send_update(self, event):
        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps({
            "message": "update",
        }))
