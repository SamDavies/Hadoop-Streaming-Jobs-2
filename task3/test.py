import os
import subprocess
import unittest


class Task3Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task3/input.txt | ' \
                       './task3/input/mapper1.py | sort -k1,1 | ./task3/input/reducer1.py |' \
                       './task3/input/mapper2.py | sort -nrk1,1 | ./task3/input/reducer2.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task3/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
