import unittest
from subprocess import Popen
from threading import Thread


class TestFunkcjiPowrotuTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionAdd
        import FunctionConsole
        self.function_global = FunctionGlobal

        self.test_id = "TS008"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(1)
        self.add_site_function_test_case = FunctionAdd.AddSiteFunctionTestCase(self.the_process)
        self.back_function_test_case = FunctionConsole.BackFunctionTestCase(self.the_process)
        self.add_site_function_test_case_2 = FunctionAdd.AddSiteFunctionTestCase(self.the_process)

    def test_funkcji_powrotu(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.add_site_function_test_case.start()
                first = False
            if self.add_site_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.add_site_function_test_case.this_log
        if not self.add_site_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.add_site_function_test_case.finished, self.test_id + ". Brak wejscia do menu funkcji dodania.")
        if " aby wrocic" not in self.add_site_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(" aby wrocic", self.add_site_function_test_case.this_log, self.test_id + ". Brak informacji o funkcji dodania.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.back_function_test_case.start()
                first = False
            if self.back_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.back_function_test_case.this_log
        if not self.back_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.back_function_test_case.finished, self.test_id + ". Brak informacji o powrocie.")
        if "Powrot" not in self.back_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("Powrot", self.back_function_test_case.this_log, self.test_id + ". Niepoprawne dzialanie funkcji powrotu.")

        self.add_site_function_test_case_2.start()
        while not self.add_site_function_test_case_2.finished:
            pass
        self.the_log += self.add_site_function_test_case_2.this_log
        if " aby wrocic" not in self.add_site_function_test_case_2.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(" aby wrocic", self.add_site_function_test_case_2.this_log, self.test_id + ". Brak poprawnego powrotu do menu glownego.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.add_site_function_test_case = None
        self.back_function_test_case = None
        self.add_site_function_test_case_2 = None
