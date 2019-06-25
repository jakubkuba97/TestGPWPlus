import unittest
from subprocess import Popen
from threading import Thread


class TestFunkcjiInformacjiBrakSpolekTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionMain
        self.function_global = FunctionGlobal

        self.test_id = "TS015"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(1)
        self.look_function_test_case = FunctionMain.LookFunctionTestCase(self.the_process)
        self.invest_function_test_case = FunctionMain.InvestFunctionTestCase(self.the_process)

    def test_funkcji_informacji_brak_spolek_1_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.look_function_test_case.start()
                first = False
            if self.look_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.look_function_test_case.this_log
        if not self.look_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_function_test_case.finished, self.test_id + ". Zle dzialanie funkcji pokazywania spolek.")
        if "nie podano" not in self.look_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nie podano", self.look_function_test_case.this_log.lower(), self.test_id + ". Brak informacji o braku spolek w bazie.")

    def test_funkcji_informacji_brak_spolek_2_czesc(self):
        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.invest_function_test_case.start()
                first = False
            if self.invest_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.invest_function_test_case.this_log
        if not self.invest_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.invest_function_test_case.finished, self.test_id + '. Zle dzialanie funkcji "/invest".')
        if "brak zapisanych" not in self.invest_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("brak zapisanych", self.invest_function_test_case.this_log.lower(), self.test_id + ". Brak informacji o braku spolek w bazie.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.look_function_test_case = None
        self.invest_function_test_case = None
