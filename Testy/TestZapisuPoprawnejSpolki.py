import unittest
from subprocess import Popen
from threading import Thread


class TestZapisuPoprawnejSpolkiTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionAdd
        import FunctionShowSites
        self.function_global = FunctionGlobal

        self.test_id = "TS007"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(10)
        self.countdown_function_3 = FunctionGlobal.CountExecution(1)
        self.add_site_function_test_case = FunctionAdd.AddSiteFunctionTestCase(self.the_process)
        self.write_correct_site_test_case = FunctionAdd.WriteCorrectSiteTestCase(self.the_process)
        self.show_sites_function_test_case = FunctionShowSites.ShowSitesFunctionTestCase(self.the_process)

    def test_zapisu_poprawnej_spolki(self):
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
            self.assertTrue(self.add_site_function_test_case.finished, self.test_id + ". Brak wejscia do menu funkcji.")
        if " aby wrocic" not in self.add_site_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(" aby wrocic", self.add_site_function_test_case.this_log, self.test_id + ". Brak informacji o funkcji.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.write_correct_site_test_case.start()
                first = False
            if self.write_correct_site_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.write_correct_site_test_case.this_log
        if not self.write_correct_site_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.write_correct_site_test_case.finished, self.test_id + ". Brak powrotu do glownego menu.")
        if "dodano do" not in self.write_correct_site_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("dodano do", self.write_correct_site_test_case.this_log, self.test_id + ". Brak informacji o poprawnym dodaniu spolki.")

        self.countdown_function_3.start()
        first = True
        while not self.countdown_function_3.finished:
            if first:
                self.show_sites_function_test_case.start()
                first = False
            if self.show_sites_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_3)
        self.the_log += self.show_sites_function_test_case.this_log
        if not self.show_sites_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.show_sites_function_test_case.finished, self.test_id + ". Brak danych wyjsciowych.")
        elif "Nazwa pliku" not in self.show_sites_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("Nazwa pliku", self.show_sites_function_test_case.this_log, self.test_id + ". Blad uruchomienia komendy.")
        elif "brak stron" in self.show_sites_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertNotIn("brak stron", self.show_sites_function_test_case.this_log, self.test_id + ". Blad zapisania spolki.")
        elif self.write_correct_site_test_case.the_data not in self.show_sites_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(self.write_correct_site_test_case.the_data, self.show_sites_function_test_case.this_log, self.test_id + ". Zapisano zla strone spolki.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.countdown_function_3 = None
        self.add_site_function_test_case = None
        self.write_correct_site_test_case = None
        self.show_sites_function_test_case = None
