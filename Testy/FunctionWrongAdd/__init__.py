from subprocess import Popen
from threading import Thread


class IncorrectSiteTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "https://kortle.com/"
        self.the_data_bytes = b"https://kortle.com/"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "wczytywanie" in output.lower():
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
            if " blad " in output:
                self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class OutsideSiteTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "https://www.bing.com/"
        self.the_data_bytes = b"https://www.bing.com/"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "wczytywanie" in output.lower():
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
            if "nie jest poprawna strona" in output:
                self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True
