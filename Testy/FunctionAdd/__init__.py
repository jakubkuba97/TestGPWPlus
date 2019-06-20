from subprocess import Popen
from threading import Thread


class AddSiteFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/add"
        self.the_data_bytes = b"/add"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if ">>> \r\n" in output:
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
        if " aby wrocic" in output:
            for i in range(2):
                self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class WriteCorrectSiteTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        import sys
        sys.path.append('../')
        import FunctionGlobal           # unknown reason for showing error - IDE bug # TODO: try to find solution
        function_global = FunctionGlobal
        self.the_data = function_global.Constants().correct_site_1
        self.the_data_bytes = self.the_data.encode('utf-8')
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b' \n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Wczytywanie!" in output:
            for i in range(3):
                self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True
