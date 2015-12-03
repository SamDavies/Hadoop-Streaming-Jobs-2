import subprocess
import unittest


class Task8Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task8/input.txt | ' \
                       './task8/input/mapper1.py | sort -nk1,1 | ./task8/input/reducer1.py | ' \
                       'cat | sort -nrk1,1 | ./task8/input/reducer2.py | ' \
                       'cat | sort -nrk1,1 | ./task8/input/reducer3.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task8/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
