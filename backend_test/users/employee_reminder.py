from dataclasses import dataclass
from datetime import date
from backend_test.notifications.slack import SlackNotification
from backend_test.notifications.slack_templates.new_menu_message import (
    get_new_menu_block_message,
)
from backend_test.meals.models import Menu
from .models import Employee


@dataclass
class EmployeeReminder:
    """Class to pick and send reminders."""

    country: str

    def get_new_menu(self):
        # TODO: Generate UUID instead of int pk
        # TODO: Call url from sites
        try:
            today_menu = Menu.objects.get(available_on=date.today())
        except Menu.DoesNotExist:
            raise
        return str(today_menu.pk)

    def get_employees_slack_ids(self):
        employees_slack_id = Employee.objects.filter(country=self.country).values_list(
            "slack_user_id", flat=True
        )
        return list(employees_slack_id)

    def send_slack_new_menu_reminder(self):
        menu_url = self.get_new_menu()
        block_message = get_new_menu_block_message(menu_url)
        slack_notification = SlackNotification(block_message, menu_url)
        recipients = self.get_employees_slack_ids()
        [
            slack_notification.send_message(recipient, user_message=True)
            for recipient in recipients
        ]
