from subprocess import Popen
from threading import Thread


class ShowSitesFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/sites"
        self.the_data_bytes = b"/sites"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Nazwa pliku" in output:
            while output != "\r\n":
                output = str(self.process.stdout.readline(), errors='ignore')
                self.this_log += output
        self.finished = True
