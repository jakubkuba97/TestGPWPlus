import unittest
from subprocess import Popen


class TestInicjujacyTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal   # unknown reason for showing error - IDE bug

        self.function_global = FunctionGlobal
        self.test_id = "TS001"
        self.function_global.ForTearDown().delete_pages_file()
        self.the_process = self.function_global.ForSetUp().launch_program()
        self.the_log = self.function_global.ForSetUp().get_first_launch_data(self.the_process)

    @staticmethod
    def clean_first_lines(process: Popen) -> str:
        temporary_output = ""
        log = ""
        while temporary_output == "" or "zaczekac" in temporary_output or temporary_output in "\r\n\t " or "Zaladowano strone" in temporary_output:
            temporary_output = str(process.stdout.readline(), errors='ignore')
            log += temporary_output
        if "zaprogramowany aby" in temporary_output:
            log += str(process.stdout.readline(), errors='ignore')
        return log

    def test_inicjujacy(self):
        temporary_log = self.function_global.CommonTestCases().write_correct_sites_name(self.the_process)
        self.the_log += temporary_log
        if "nowy plik" not in temporary_log:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nowy plik", temporary_log, "Brak informacji o stoworzeniu nowego pliku ze stronami!")
        temporary_log = self.clean_first_lines(self.the_process)
        self.the_log += temporary_log
        if " aby dowiedziec sie wiecej o programie" not in temporary_log:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(" aby dowiedziec sie wiecej o programie", temporary_log, "Brak pojawienia sie podstawowych informacji o programie!")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
