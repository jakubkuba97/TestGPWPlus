from subprocess import Popen
from threading import Thread


class IncorrectSiteDetailsTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/look-" + "qqqqqq"
        self.the_data_bytes = b"/look-" + b"qqqqqq"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Nie podano poprawnej" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class IncorrectSiteRemovalTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/remove-" + "qqqqqq"
        self.the_data_bytes = b"/remove-" + b"qqqqqq"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Nie podano poprawnej" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True
