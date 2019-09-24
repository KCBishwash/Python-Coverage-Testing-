import unittest
from unittest.mock import patch
import io
from io import StringIO
import sys
from tigr.parser.peg_parser import PEGParser
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker

class TestCasePegParser(unittest.TestCase):

    mock_out = patch('sys.stdout', new_callable=StringIO)
    mock_err = patch('sys.stderr', new_callable=io.StringIO)

    def setUp(self):
        self.instance = PEGParser(Drawer(TurtleWorker()))

    # def tearDown(self):
        # self.mock_out.truncate(0)
        # self.mock_out.seek(0)
        # self.mock_err.truncate(0)
        # self.mock_err.seek(0)

    def test_parse_invalid_statements(self):
        file = [
            ['cs okoks'],
            ['cdsicjssoi']
        ]
        for test_statement in file:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.instance.parse(test_statement)
                self.assertTrue(fake_out.getvalue().startswith('Invalid command:'))


    def test_parse_comment(self):

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.instance.parse('#')
            print()
            self.assertTrue(fake_out.getvalue().startswith('comment found: '))



    def test_parse_empty_lines(self):

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.instance.parse('')
            print()
            self.assertEqual(fake_out.getvalue().strip(), '')


