'''
syntax:
mock.patch('package.module.ClassName',
    return_value='bar',
    side_effect=Exception('boom!'))

3 ways of applying a mock:
    - decorator
    - context manager
    - inline
'''

from unittest import mock, TestCase
from project import fs


class TestExample(TestCase):
    @mock.patch('project.fs.check_output', return_value=b'foo\nbar\n')
    def test_print_contents(self, mock_check_output):
        actual_reuslts = fs.print_contents()

        expected_directory = b'foo'
        self.assertIn(expected_directory, actual_reuslts)
