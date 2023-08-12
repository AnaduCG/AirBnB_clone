#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('builtins.input', side_effect=['quit'])
    def test_quit_command(self, mock_input):
        cmd = HBNBCommand()
        """ Enters the command loop """
        cmd.cmdloop()
        """ Check if the command loop is exited """
        self.assertTrue(cmd.do_quit)


if __name__ == "__main__":
    unittest.main()
