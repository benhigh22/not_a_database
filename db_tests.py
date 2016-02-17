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

    def test_db_reader_can_get_record_by_name_as_a_list(self):
        file_input = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username("bhigh"),["bhigh"])

    def test_db_reader_can_get_record_by_username_as_a_list_in_any_case(self):
        file_input = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username("BHIgh"),["bhigh"])

    @mock.patch("db.DBReader.read_file")
    def test_db_reader_will_read_from_database_if_no_contents_provided(self, read_file):
        read_file.return_value = ["bhigh,password,benjamin high,26,160", "mhigh,1234,marisa high,25,115"]
        db_reader = DBReader()
        read_file.assert_called_once_with()

    def test_db_reader_get_by_username_raises_error_if_multiple_people_with_same_name(self):
        file_input = ["bhigh,password,benjamin high,26,160", "bhigh,password,bob high,77,180"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username("asdf"),("No records found for that username."))

    def test_db_reader_get_info_from_correct_password_entry(self):
        file_input = ["bhigh,password,benjamin high,26,160"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_password("password"),["benjamin high","26","160"])

    def test_db_reader_get_info_from_incorrect_password_entry(self):
        file_input = ["bhigh,password,benjamin high,26,160"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_password("asdf"),("No records found for that password."))
