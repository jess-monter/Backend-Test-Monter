# Utilities for template building.


def get_new_menu_block_message(menu_url):  # pragma: no cover
    """Build a message with a custom menu url."""
    return [
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hello, stranger.\n Today's menu is ready.",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Go To Menu", "emoji": True},
                "value": "choose_your_meal",
                "url": menu_url,
                "action_id": "button-action",
            },
        },
        {"type": "divider"},
    ]
