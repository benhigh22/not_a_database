import unittest

from unittest import mock

from db import DBReader


class DBTestCase(unittest.TestCase):


    def test_db_reader_can_format_expected_file_structure(self):
        expected_input = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        expected_output = [["bhigh","password","benjamin high","26","160"], ["mhigh","1234","marisa high","25","115"]]
        self.assertEqual(DBReader.clean_file(expected_input), expected_output)

    def test_db_reader_can_format_expected_file_structure_in_init(self):
        expected_input = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        expected_output = [["bhigh","password","benjamin high","26","160"], ["mhigh","1234","marisa high","25","115"]]
        db_reader = DBReader(expected_input)
        self.assertEqual(db_reader.cleaned_data, expected_output)

    @mock.patch("db.DBReader.read_file")
    def test_db_reader_will_read_from_database_if_no_contents_provided(self, read_file):
        read_file.return_value = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        db_reader = DBReader()
        read_file.assert_called_once_with()

    def test_db_reader_get_info_from_correct_password_entry(self):
        file_input = ["bhigh,password,benjamin high,26,160"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username_password("bhigh", "password"),["benjamin high","26","160"])

    def test_db_reader_get_info_from_incorrect_password_entry(self):
        file_input = ["bhigh,password,benjamin high,26,160"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username_password("asdf", "adfdsf"),("Either your username or password is incorrect."))

