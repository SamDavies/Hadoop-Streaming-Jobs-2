import os
import subprocess
import unittest


class Task7Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task7/input.txt | ' \
                       './task7/input/mapper1.py | sort -nrk1,1 | ./task7/input/reducer1.py | ' \
                       'cat | sort -nrk1,1 | ./task7/input/reducer2.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task7/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
