import os
import subprocess
import unittest


class Task3Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task5/input.txt | ' \
                       './task5/input/mapper1.py | sort -k1,1 | ./task5/input/reducer1.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task5/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
