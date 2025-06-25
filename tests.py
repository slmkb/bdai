import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    
    def test_cwd(self):
        res = get_files_info("calculator", ".")
        print('Testing get_files_info("calculator", ".")')
        print(res)
        print()

    def test_pkg(self):
        res = get_files_info("calculator", "pkg")
        print('Testing get_files_info("calculator", "pkg")')
        print(res)
        print()

    def test_bin(self):
        res = get_files_info("calculator", "/bin")
        print('Testing get_files_info("calculator", "/bin")')
        print(res)
        print()

    def test_traversal(self):
        res = get_files_info("calculator", "../")
        print('Testing get_files_info("calculator", "../")')
        print(res)
        print()

class TestGetFilesContents(unittest.TestCase):
    
    def test_main(self):
        res = get_file_content("calculator", "main.py")
        print('Testing get_file_content("calculator", "main.py")')
        print(res)
        print()

    def test_pkg(self):
        res = get_file_content("calculator", "pkg/calculator.py")
        print('Testing get_file_content("calculator", "pkg/calculator.py")')
        print(res)
        print()

    def test_bin(self):
        res = get_file_content("calculator", "/bin/cat")
        print('Testing get_file_content("calculator", "/bin/cat")')
        print(res)
        print()

    def test_lorem(self):
        res = get_file_content("calculator", "lorem.txt")
        print('Testing get_file_content("calculator", "lorem.txt")')
        print(res)
        print()

class TestWriteFilesContents(unittest.TestCase):
    
    def test_overwrite(self):
        res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print('Testing write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
        print(res)
        print()

    def test_new_file(self):
        res = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print('Testing write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
        print(res)
        print()

    def test_fail(self):
        res = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print('Testing write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
        print(res)
        print()

class TestRunFile(unittest.TestCase):
    
    def test_run_main(self):
        res = run_python_file("calculator", "main.py")
        print('Testing run_python_file("calculator", "main.py")')
        print(res)
        print()

    def test_run_test(self):
        res = run_python_file("calculator", "tests.py")
        print('Testing run_python_file("calculator", "tests.py")')
        print(res)
        print()

    def test_run_traversal(self):
        res = run_python_file("calculator", "../main.py")
        print('Testing run_python_file("calculator", "../main.py")')
        print(res)
        print()

    def test_run_nonexistent(self):
        res = run_python_file("calculator", "nonexistent.py")
        print('Testing run_python_file("calculator", "nonexistent.py")')
        print(res)
        print()

if __name__ == "__main__":
    unittest.main()