from subprocess import Popen


class Constants:
    def __init__(self):
        self.pages_name = "Strony"
        self.pages_bytes_name = b"Strony"

    @staticmethod
    def get_path_to_program() -> str:
        from os import path
        path_to_project = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
        path_to_program = (path_to_project + r"\Dokumentacja\Przedmiot testow")
        return path_to_program

    @staticmethod
    def get_path_to_temporary_logs() -> str:
        from os import path
        path_to_project = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
        path_to_temporary_logs = (path_to_project + r"\Testy\Tymczasowe historie")
        return path_to_temporary_logs


class ForSetUp:
    @staticmethod
    def launch_program() -> Popen:
        from subprocess import PIPE, STDOUT
        path_to_program = Constants().get_path_to_program()
        the_main_process = Popen(['GPWPlus.exe', '-show_streams', path_to_program], shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT, cwd=path_to_program)
        return the_main_process

    @staticmethod
    def get_first_launch_data(the_process: Popen) -> str:
        output = ""
        for j in range(3):
            output += str(the_process.stdout.readline(), errors='ignore')
        if "znaleziono pliku ze stronami" not in output:
            raise ValueError("This is not the first launch! Use different function!")
        return output


class ForTearDown:
    @staticmethod
    def close_program(the_process: Popen):
        try:
            the_process.terminate()
            the_process.wait()
        except AttributeError:
            pass

    @staticmethod
    def delete_pages_file():
        try:
            from os import remove
            path_to_program = Constants().get_path_to_program()
            remove(path_to_program + "\\" + Constants().pages_name + ".txt")
        except FileNotFoundError:
            pass

    @staticmethod
    def save_log_to_file(test_scenario_id: str, log_output: str):
        path_to_temporary_logs = Constants().get_path_to_temporary_logs()
        with open(path_to_temporary_logs + "\\" + test_scenario_id + ".txt", 'w') as new_file:
            new_file.write(log_output)


class CommonTestCases:
    @staticmethod
    def write_correct_sites_name(the_process: Popen) -> str:
        the_process.stdin.write(Constants().pages_bytes_name + b'\n')
        the_process.stdin.flush()
        output = ""
        for i in range(2):
            output += str(the_process.stdout.readline(), errors='ignore')
            if "Zla " in output:
                break
            if ":" in output and i == 0:
                output = output.replace(":", ': ' + Constants().pages_name + '\n\t')
        return output
