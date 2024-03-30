"""
Test wait_db command
"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_db.Command.check")
class CommandWaitDbTestCase(SimpleTestCase):
    def test_wait_db(self, patched_check):
        """
        Test Waiting for Database Command if Database is Ready
        """
        patched_check.return_value = True
        call_command("wait_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_db_delay(self, patched_sleep, patched_check):
        patched_check.side_effect = (
            [Psycopg2OperationalError] * 2 + [OperationalError] * 4 + [True]
        )
        call_command("wait_db")
        self.assertEqual(patched_check.call_count, 7)
        patched_check.assert_called_with(databases=["default"])
