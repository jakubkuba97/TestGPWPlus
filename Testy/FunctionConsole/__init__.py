from subprocess import Popen
from threading import Thread


class BackFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/back"
        self.the_data_bytes = b"/back"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Powrot" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class ClearFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/space"
        self.the_data_bytes = b"/space"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if output == ">>> \x0c\r\n":
            self.this_log += str("<- cleared console ->")
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class ExitFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/exit"
        self.the_data_bytes = b"/exit"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n' + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if output == '>>> XXX ':
            self.this_log += str("\n<- exited ->\n")
            self.finished = True
