from subprocess import Popen
from threading import Thread


class FunctionHelpTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/help"
        self.the_data_bytes = b"/help"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        self.this_log += str(self.process.stdout.readline(), errors='ignore')
        temporary_output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += temporary_output
        while temporary_output != ">>> \r\n" and "Wyjscie" not in temporary_output:
            temporary_output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += temporary_output
        if "Wyjscie" in temporary_output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class FunctionInfoTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/info"
        self.the_data_bytes = b"/info"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if ">>> \r\n" in self.this_log:
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
        if "Jestem programem " in output:
            while "Program dziala w pelni " not in output:
                output = str(self.process.stdout.readline(), errors='ignore')
                self.this_log += output
        self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True
