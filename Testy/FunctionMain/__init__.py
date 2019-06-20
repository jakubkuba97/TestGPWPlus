from subprocess import Popen
from threading import Thread


class LookFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/look"
        self.the_data_bytes = b"/look"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        if "Nie podano" in output:
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        elif ">>> " in output:
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
            while output != "\r\n":
                output = str(self.process.stdout.readline(), errors='ignore')
                self.this_log += output
        self.finished = True


class RemoveOneSiteFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        import sys
        sys.path.append('../')
        import FunctionGlobal               # unknown reason for showing error - IDE bug # TODO: try to find solution
        function_global = FunctionGlobal
        self.the_data = "/remove-" + function_global.Constants().correct_site_1
        self.the_data_bytes = self.the_data.encode('utf-8')
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.this_log += str(self.process.stdout.readline(), errors='ignore')
        # output = str(self.process.stdout.readline(), errors='ignore')
        # self.this_log += output
        # if "Brak spolek" in output:
        #     self.this_log += str(self.process.stdout.readline(), errors='ignore')
        # elif ">>> " in output:
        #     if "Usunieto strone" in output:
        #         self.this_log += str(self.process.stdout.readline(), errors='ignore')
        #     elif "Nie podano poprawnej" in output:
        #         self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class ClearFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        """
        Note that this test case is expected to time out.
        """
        self.daemon = True
        self.the_data = "/clear"
        self.the_data_bytes = b"/clear"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class DeletionApprovalTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "y"
        self.the_data_bytes = b"y"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        for i in range(4):
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class LookOneSiteFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        import sys
        sys.path.append('../')
        import FunctionGlobal               # unknown reason for showing error - IDE bug # TODO: try to find solution
        function_global = FunctionGlobal
        self.the_data = "/look-" + function_global.Constants().correct_site_1
        self.the_data_bytes = self.the_data.encode('utf-8')
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        for i in range(6):
            self.this_log += str(self.process.stdout.readline(), errors='ignore')
        self.finished = True


class InvestFunctionTestCase(Thread):
    def __init__(self, process: Popen):
        Thread.__init__(self)
        self.daemon = True
        self.the_data = "/invest"
        self.the_data_bytes = b"/invest"
        self.process = process
        self.this_log = ""
        self.finished = False

    def run(self) -> None:
        self.process.stdin.write(self.the_data_bytes + b'\n')
        self.process.stdin.flush()
        self.this_log = "\t" + self.the_data + "\n"
        output = str(self.process.stdout.readline(), errors='ignore')
        self.this_log += output
        while output != "\r\n":
            output = str(self.process.stdout.readline(), errors='ignore')
            self.this_log += output
        self.finished = True
