from subprocess import Popen
from threading import Thread


class ShowSitesFunctionTestCase(Thread):
    """
    This Test Case is expected to time out, since it is impossible
    to predict how many lines it will need to read!
    """
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/sites"
        self.the_data_bytes = b"/sites"
        self.process = process
        self.this_log = ""
        self.finished = False       # leave for consistency

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Nazwa pliku" in output:
            while True:
                self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True        # set to true only if unexpected input request is received
