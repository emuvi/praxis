import threading
import unittest
from time import sleep, time


def scheduler(function, milliseconds):
    def sleep_then_call(milliseconds):
        sleep(milliseconds / 1000)
        function()
    threading.Thread(target = sleep_then_call, args = [milliseconds]).start()


class Scheduler():
    def __init__(self):
        self.functions = []
        threading.Thread(target = self._poll).start()
    
    def _poll(self):
        while True:
            sleep(0.0010)
            now = time() * 1000
            remains = []
            while self.functions:
                function, due_time = self.functions.pop()
                if now >= due_time:
                    function()
                else:
                    remains.append((function, due_time))
            self.functions.extend(remains)

    def delay(self, function, milliseconds):
        self.functions.append((function, time() * 1000 + milliseconds))



class Tester(unittest.TestCase):
    def test_case_01(self):
        def function():
            print("Test")
        scheduler(function, 1000)
    
    def test_case_02(self):
        sch = Scheduler()
        def function():
            print("Test")
        sch.delay(function, 1000)


if __name__ == '__main__':
    unittest.main()
