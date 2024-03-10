#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import os


class TestConsole(unittest.TestCase):
    def test_help(self):
        """Test help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            HBNBCommand().onecmd(f"show BaseModel {id_created}")
            self.assertIn(id_created, f.getvalue())

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {id_created}")
            HBNBCommand().onecmd(f"show BaseModel {id_created}")
            self.assertIn("** no instance found **", f.getvalue())

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_created = f.getvalue().strip()
            HBNBCommand().onecmd(f"update BaseModel {id_created} name 'test'")
            HBNBCommand().onecmd(f"show BaseModel {id_created}")
            self.assertIn("'name': 'test'", f.getvalue())

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))

if __name__ == "__main__":
    unittest.main()
