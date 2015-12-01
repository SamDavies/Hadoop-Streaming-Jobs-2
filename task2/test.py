import os
import subprocess
import unittest


class Task9Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task2/input.txt | ' \
                       './task2/input/mapper1.py | sort -nk1,1 | ./task2/input/reducer1.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task2/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
