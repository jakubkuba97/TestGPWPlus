import unittest
from subprocess import Popen
from threading import Thread


class TestFunkcjiDodatkowychInformacjiTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionInfo
        self.function_global = FunctionGlobal

        self.test_id = "TS006"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.function_info_test_case = FunctionInfo.FunctionInfoTestCase(self.the_process)

    def test_funkcji_pomocy(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.function_info_test_case.start()
                first = False
            if self.function_info_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.function_info_test_case.this_log
        if not self.function_info_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.function_info_test_case.finished, self.test_id + ". Brak pokazania sie wszystkich informacji.")
        if "Jestem programem " not in self.function_info_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("Jestem programem ", self.function_info_test_case.this_log, self.test_id + ". Brak niezbednych informacji.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.function_help_test_case = None
