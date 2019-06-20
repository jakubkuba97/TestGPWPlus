from subprocess import Popen
from threading import Thread


class AlphabeticalSortTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/sort-a"
        self.the_data_bytes = b"/sort-a"
        self.process = process
        self.this_log = ""
        self.finished = False
        self.no_sites_read = True       # true if no sites were read

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Brak spolek" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        elif "Wysortowano spolki" in output:
            self.no_sites_read = False
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class PercentageSortTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/sort-p"
        self.the_data_bytes = b"/sort-p"
        self.process = process
        self.this_log = ""
        self.finished = False
        self.no_sites_read = True       # true if no sites were read

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Brak spolek" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        elif "Wysortowano spolki" in output:
            self.no_sites_read = False
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True
