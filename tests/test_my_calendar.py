import unittest
from src.calendar_util import my_calendar
from unittest.mock import patch
from unittest.mock import Mock
from datetime import datetime
from requests.exceptions import Timeout


class TestMyCalendar(unittest.TestCase):

    # Patch as a Decorator
    @patch('src.calendar_util.my_calendar.datetime')
    def test_today_is_a_weekday(self, mock_datetime):
        monday = datetime(year=2020, month=7, day=6)
        saturday = datetime(year=2020, month=7, day=4)
        mock_datetime.today.side_effect = [monday, saturday]

        # check for a monday
        self.assertTrue(my_calendar.today_is_a_weekday())

        # check for a saturday
        self.assertFalse(my_calendar.today_is_a_weekday())

    # Patch as a Context Manager
    def test_get_holidays(self):
        with patch('src.calendar_util.my_calendar.requests') as mock_requests:
            response_mock = Mock()
            response_mock.status_code = 200
            response_mock.json.return_value = {
                '12/25': 'Christmas',
                '01/01': 'New Year',
            }
            mock_requests.get.return_value = response_mock
            holidays_response = my_calendar.get_holidays()
            self.assertIsNotNone(holidays_response)
            self.assertEqual("Christmas", holidays_response['12/25'])
            self.assertEqual("New Year", holidays_response['01/01'])

    # Patching an Object’s Attributes
    @patch.object(my_calendar.requests, 'get', side_effect=Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(Timeout):
            my_calendar.get_holidays()


if __name__ == '__main__':
    unittest.main()

