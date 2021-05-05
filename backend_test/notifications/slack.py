from django.conf import settings
from dataclasses import dataclass
from slack_bolt import App
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


@dataclass
class SlackNotification:

    channel_name: str
    block_message: str
    text_message: str = None
    user_message: bool = False

    @property
    def client(self):
        return WebClient(token=settings.SLACK_BOT_TOKEN)

    def get_channel_id(self):
        """ Get channel id by name from slack. """
        conversation_id = None
        try:
            con = self.client.conversations_list()
            channels = list(
                filter(
                    lambda channel: channel["name"] == self.channel_name,
                    con.data["channels"],
                )
            )
            if channels:
                conversation_id = channels[0]["id"]
        except SlackApiError as error:
            raise
        return conversation_id

    def send_message(self):
        recipient = self.channel_name if self.user_message else self.get_channel_id()
        try:
            self.client.chat_postMessage(
                channel=recipient, text=self.text_message, blocks=self.block_message
            )
        except SlackApiError as error:
            raise
