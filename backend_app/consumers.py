import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging
logging.basicConfig(
    level=logging.INFO,  # Show INFO level logs and above
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Use the logger
logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = str(data.get('message', ''))  # Ensure this is a string
        sender = str(data.get('sender', ''))    # Ensure this is a string
        receiver = str(data.get('receiver', ''))
        logger.info(f"Received message: {message} from {sender} to {receiver}")
        await self.save_message(sender, receiver, message)

        # Broadcast message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'receiver': receiver
            }
        )

    async def chat_message(self, event):
        message = str(event['message'])  # Ensure message is a string
        sender = str(event['sender'])    # Ensure sender is a string
        receiver = str(event['receiver'])

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'receiver': receiver
        }))

    @staticmethod
    async def save_message(sender, receiver, message):
        from asgiref.sync import sync_to_async
        from .models import Message
        await sync_to_async(Message.objects.create)(
            sender=sender,
            receiver=receiver,
            message=message,
        )
