from django.conf import settings
from dataclasses import dataclass
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


@dataclass
class SlackNotification:
    """Class to handle slack notifications."""

    block_message: str
    text_message: str

    @property
    def client(self):
        """Start slack client."""
        return WebClient(token=settings.SLACK_BOT_TOKEN)

    def get_channel_id(self, channel_name):
        """Get channel id by name from slack."""
        conversation_id = None
        try:
            con = self.client.conversations_list()
            channels = list(
                filter(
                    lambda channel: channel["name"] == channel_name,
                    con.data["channels"],
                )
            )
            if channels:
                conversation_id = channels[0]["id"]
        except SlackApiError as error:
            raise
        return conversation_id

    def send_message(self, channel_name=None, user_message=False):
        """Send slack message to user or channel."""
        recipient = channel_name if user_message else self.get_channel_id(channel_name)
        try:
            self.client.chat_postMessage(
                channel=recipient, text=self.text_message, blocks=self.block_message
            )
        except SlackApiError as error:
            raise
