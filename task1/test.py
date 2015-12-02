import os
import subprocess
import unittest


class Task1Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command1 = 'cat task1/input1.txt | ' \
                        './task1/input/mapper1.py'
        bash_command2 = 'cat task1/input2.txt | ' \
                        './task1/input/mapper1.py'
        bash_command3 = 'cat task1/input3.txt | ' \
                        './task1/input/mapper1.py'
        os.environ["mapreduce_map_input_file"] = 'task1/input1.txt'
        output = subprocess.check_output(bash_command1, shell=True)
        os.environ["mapreduce_map_input_file"] = 'task1/input2.txt'
        output += subprocess.check_output(bash_command2, shell=True)
        os.environ["mapreduce_map_input_file"] = 'task1/input3.txt'
        output += subprocess.check_output(bash_command3, shell=True)
        with open("task1/temp.txt", "w") as text_file:
            text_file.write(output)

        bash_command4 = 'cat task1/temp.txt | ' \
                        'sort -k1,1 | ./task1/input/reducer1.py | sort -k1,1 | ./task1/input/reducer2.py'
        output = subprocess.check_output(bash_command4, shell=True)

        # when
        expected = subprocess.check_output('cat task1/output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
