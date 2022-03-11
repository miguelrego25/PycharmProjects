##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.pacman import pacman
from Root.src.deadcode import deadcode

import unittest

class deadcodeTest(unittest.TestCase):

    def test_deadcode_1(self):
        with test_timeout(self,1):
            prog = ["print 0","jump 0,2","print 1","jump 2,4"]
            self.assertEqual(deadcode(prog),(4,0))

    def test_deadcode_2(self):
        with test_timeout(self,1):
            prog = ["print 0","jump 0,3","print 2","print 1","jump 3,5"]
            self.assertEqual(deadcode(prog),(4,1))

class pacmanTest(unittest.TestCase):

    def test_pacman_1(self):
        with test_timeout(self,1):
            mapa = ["*****",
                    "*  G*",
                    "* ***",
                    "*P G*",
                    "*****"]
            self.assertEqual(pacman(mapa),(1,2))

    def test_pacman_2(self):
        with test_timeout(self,1):
            mapa = ["******",
                    "P G   ",
                    "******"]
            self.assertEqual(pacman(mapa),(5,1))

if __name__ == '__main__':
    unittest.main()

import time
import signal

class TestTimeout(Exception):
    pass

class test_timeout:
  def __init__(self, test, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message
    self.test = test

  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)
    if exc_type is not None and exc_type is not AssertionError:
        self.test.fail("execution error")