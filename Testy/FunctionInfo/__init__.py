from subprocess import Popen


class FunctionHelpTestCase:
    def __init__(self):
        self.the_data = "/help"
        self.the_data_bytes = b"/help"

    def launch_help_function(self, process: Popen) -> str:
        process.stdin.write(self.the_data_bytes + b'\n')
        process.stdin.flush()
        output = "\t" + self.the_data + "\n"
        output += str(process.stdout.readline(), errors='ignore')
        temporary_output = str(process.stdout.readline(), errors='ignore')
        output += temporary_output
        while temporary_output != ">>> \r\n" and "Wyjscie" not in temporary_output:
            temporary_output = str(process.stdout.readline(), errors='ignore')
            output += temporary_output
        if "Wyjscie" in temporary_output:
            output += str(process.stdout.readline(), errors='ignore')
        return output


class FunctionInfoTestCase:
    def __init__(self):
        self.the_data = "/info"
        self.the_data_bytes = b"/info"

    def launch_info_function(self, process: Popen) -> str:
        # TODO: remember to fix this function!
        process.stdin.write(self.the_data_bytes + b'\n')
        process.stdin.flush()
        output = self.the_data + "\n"
        output += str(process.stdout.readline(), errors='ignore')
        return output