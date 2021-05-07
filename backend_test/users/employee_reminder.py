from dataclasses import dataclass
from datetime import date
from django.contrib.sites.models import Site

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
        """Get todays menu str uuid."""
        try:
            today_menu = Menu.objects.get(available_on=date.today())
        except Menu.DoesNotExist:
            raise
        return str(today_menu.pk)

    def get_site_domain(self):
        """Get domain from current site."""
        current_site = Site.objects.get_current()
        return current_site.domain

    def get_menu_url(self):
        """Get menu url built."""
        domain = self.get_site_domain()
        menu = self.get_new_menu()
        return domain + menu

    def get_employees_slack_ids(self):
        """Get employees to send notifications."""
        employees_slack_id = (
            Employee.objects.filter(country=self.country)
            .exclude(slack_user_id__in=[None, ""])
            .values_list("slack_user_id", flat=True)
        )
        return list(employees_slack_id)

    def send_slack_new_menu_reminder(self):
        """Send notifications to right employees to slack."""
        menu_url = self.get_menu_url()
        block_message = get_new_menu_block_message(menu_url)
        slack_notification = SlackNotification(block_message, menu_url)
        recipients = self.get_employees_slack_ids()
        [
            slack_notification.send_message(recipient, user_message=True)
            for recipient in recipients
        ]
