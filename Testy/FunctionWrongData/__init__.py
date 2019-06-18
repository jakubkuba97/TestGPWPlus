from subprocess import Popen


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


class MeaninglessCharsTestCase:
    def __init__(self):
        self.the_data = "asdf"
        self.the_data_bytes = b"asdf"

    def write_meaningless_chars(self, process: Popen) -> str:
        process.stdin.write(self.the_data_bytes + b'\n')
        process.stdin.flush()
        output = self.the_data + "\n"
        output += str(process.stdout.readline(), errors='ignore')
        return output


class WrongCommandTestCase:
    def __init__(self):
        self.the_data = "/obliviate"
        self.the_data_bytes = b"/obliviate"

    def write_wrong_command(self, process: Popen) -> str:
        process.stdin.write(self.the_data_bytes + b'\n')
        process.stdin.flush()
        output = self.the_data + "\n"
        output += str(process.stdout.readline(), errors='ignore')
        return output
