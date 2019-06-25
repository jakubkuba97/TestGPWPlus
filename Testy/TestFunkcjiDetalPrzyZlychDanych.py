import unittest
from subprocess import Popen
from threading import Thread


class TestFunkcjiDetalPrzyZlychDanychTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionWrongMain
        self.function_global = FunctionGlobal

        self.test_id = "TS016"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_1_site_saved()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.incorrect_site_details_test_case = FunctionWrongMain.IncorrectSiteDetailsTestCase(self.the_process)
        self.incorrect_site_removal_test_case = FunctionWrongMain.IncorrectSiteRemovalTestCase(self.the_process)

    def test_funkcji_detal_przy_zlych_danych_1_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.incorrect_site_details_test_case.start()
                first = False
            if self.incorrect_site_details_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.incorrect_site_details_test_case.this_log
        if not self.incorrect_site_details_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.incorrect_site_details_test_case.finished, self.test_id + ". Zle dzialanie funkcji pokazania jednej spolki.")
        elif "nie podano poprawnej" not in self.incorrect_site_details_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nie podano poprawnej", self.incorrect_site_details_test_case.this_log.lower(), self.test_id + ". Brak informacji o niepoprawnej spolce.")

    def test_funkcji_detal_przy_zlych_danych_2_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.incorrect_site_removal_test_case.start()
                first = False
            if self.incorrect_site_removal_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.incorrect_site_removal_test_case.this_log
        if not self.incorrect_site_removal_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.incorrect_site_removal_test_case.finished, self.test_id + ". Zle dzialanie funkcji usuniecia jednej spolki.")
        elif "nie podano poprawnej" not in self.incorrect_site_removal_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nie podano poprawnej", self.incorrect_site_removal_test_case.this_log.lower(), self.test_id + ". Brak informacji o niepoprawnej spolce.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.incorrect_site_details_test_case = None
        self.incorrect_site_removal_test_case = None
