import unittest
from subprocess import Popen
from threading import Thread


class TestZapisuStronyPozaBazaTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionAdd
        import FunctionWrongAdd
        self.function_global = FunctionGlobal

        self.test_id = "TS011"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(3)
        self.add_site_function_test_case = FunctionAdd.AddSiteFunctionTestCase(self.the_process)
        self.outside_site_test_case = FunctionWrongAdd.OutsideSiteTestCase(self.the_process)

    def test_zapisu_strony_poza_baza(self):
        # https://www.bing.com/
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
            self.assertTrue(self.add_site_function_test_case.finished, self.test_id + ". Brak wejscia do menu funkcji i pojawienia sie informacji o niej.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.outside_site_test_case.start()
                first = False
            if self.outside_site_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.outside_site_test_case.this_log
        if not self.outside_site_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.outside_site_test_case.finished, self.test_id + ". Brak informacji o zlych danych przy zlej stronie.")
        if "nie jest poprawna strona" not in self.outside_site_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nie jest poprawna strona", self.outside_site_test_case.this_log, self.test_id + ". Brak informacji o zlej stronie.")
        if "dodano" in self.outside_site_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertNotIn("dodano", self.outside_site_test_case.this_log.lower(), self.test_id + ". Informacja o zapisie strony.")

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
        self.outside_site_test_case = None
