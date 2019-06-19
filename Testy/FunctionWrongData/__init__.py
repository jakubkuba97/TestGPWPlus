from subprocess import Popen
from threading import Thread


class BlankDataWrittenTestCase:
    @staticmethod
    def write_blank_data(process: Popen) -> str:
        process.stdin.write(b'\n')
        process.stdin.flush()
        output = "\n"
        output += str(process.stdout.readline(), errors='ignore')
        return output


class DataWrongForFileSavingTestCase:
    def __init__(self):
        self.the_data = "\\/"
        self.the_data_bytes = b"\\/"

    def write_wrong_file_saving_data(self, process: Popen) -> str:
        process.stdin.write(self.the_data_bytes + b'\n')
        process.stdin.flush()
        output = self.the_data + "\n"
        output += str(process.stdout.readline(), errors='ignore')
        return output


class MeaninglessCharsTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "asdf"
        self.the_data_bytes = b"asdf"
        self.process = process
        self.this_log = ""

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        output = self.the_data + "\n"
        output += str(self.process.stdout.readline(), errors='ignore')
        self.this_log = output


class WrongCommandTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/obliviate"
        self.the_data_bytes = b"/obliviate"
        self.process = process
        self.this_log = ""

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        output = self.the_data + "\n"
        output += str(self.process.stdout.readline(), errors='ignore')
        self.this_log = output
