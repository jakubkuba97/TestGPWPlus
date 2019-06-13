from subprocess import Popen


class Constants:
    @staticmethod
    def get_path_to_program() -> str:
        from os import path
        path_to_project = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
        path_to_program = (path_to_project + r"\Dokumentacja\Przedmiot testow")
        return path_to_program


class ForSetUp:
    @staticmethod
    def launch_program() -> Popen:
        from subprocess import PIPE, STDOUT
        path_to_program = Constants().get_path_to_program()
        the_main_process = Popen(['GPWPlus.exe', '-show_streams', path_to_program], shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        return the_main_process


class ForTearDown:
    @staticmethod
    def close_program(the_process: Popen):
        the_process.terminate()


class CommonFunctions:
    pass


# use only for debug
if __name__ == '__main__':
    x = ForSetUp().launch_program()
    ForTearDown().close_program(x)
