import unittest
from subprocess import Popen
from threading import Thread


class TestFunkcjiKonsoliTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionConsole
        self.function_global = FunctionGlobal

        self.test_id = "TS009"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(2)
        self.countdown_function_2 = FunctionGlobal.CountExecution(3)
        self.clear_function_test_case_1 = FunctionConsole.ClearFunctionTestCase(self.the_process)
        self.clear_function_test_case_2 = FunctionConsole.ClearFunctionTestCase(self.the_process)
        self.exit_function_test_case = FunctionConsole.ExitFunctionTestCase(self.the_process)

    def test_funkcji_konsoli_1_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.clear_function_test_case_1.start()
                first = False
            if self.clear_function_test_case_1.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.clear_function_test_case_1.this_log
        if not self.clear_function_test_case_1.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.clear_function_test_case_1.finished, self.test_id + ". Brak reakcji na komende.")
        if ">>> \x0c\r\n" not in self.clear_function_test_case_1.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(">>> \x0c\r\n", self.clear_function_test_case_1.this_log, self.test_id + ". Blad wyczyszczenia konsoli.")

        self.clear_function_test_case_2.start()
        while not self.clear_function_test_case_2.finished:
            pass
        self.the_log += self.clear_function_test_case_2.this_log
        if ">>> \x0c\r\n" not in self.clear_function_test_case_2.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(">>> \x0c\r\n", self.clear_function_test_case_2.this_log, self.test_id + ". Blad pozostania w glownym menu!.")

    def test_funkcji_konsoli_2_czesc(self):
        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.exit_function_test_case.start()
                first = False
            if self.exit_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.exit_function_test_case.this_log
        if not self.exit_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.exit_function_test_case.finished, self.test_id + ". Brak reakcji na komende.")
        if ">>> XXX " not in self.exit_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(">>> XXX ", self.exit_function_test_case.this_log, self.test_id + ". Blad wyjscia z programu.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.clear_function_test_case_1 = None
        self.clear_function_test_case_2 = None
        self.exit_function_test_case = None
