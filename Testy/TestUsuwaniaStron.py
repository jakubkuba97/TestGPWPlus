import unittest
from subprocess import Popen
from threading import Thread


class TestUsuwaniaStronTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionMain
        self.function_global = FunctionGlobal

        self.test_id = "TS013"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_3_sites_saved()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(2)
        self.countdown_function_3 = FunctionGlobal.CountExecution(2)
        self.look_function_test_case = FunctionMain.LookFunctionTestCase(self.the_process)
        self.remove_one_site_function_test_case = FunctionMain.RemoveOneSiteFunctionTestCase(self.the_process)
        self.clear_function_test_case = FunctionMain.ClearFunctionTestCase(self.the_process)
        self.deletion_approval_test_case = FunctionMain.DeletionApprovalTestCase(self.the_process)

    def test_usuwania_stron_1_czesc(self):
        # https://www.gpw.pl/spolka?isin=PL11BTS00015
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.remove_one_site_function_test_case.start()
                first = False
            if self.remove_one_site_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.remove_one_site_function_test_case.this_log
        if not self.remove_one_site_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.remove_one_site_function_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji usuwania jednej spolki.")
        if "brak spolek" in self.remove_one_site_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertNotIn("brak spolek", self.remove_one_site_function_test_case.this_log.lower(), self.test_id + ". Blad znalezienia zadnych spolek.")
        if "nie podano poprawnej" in self.remove_one_site_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertNotIn("nie podano poprawnej", self.remove_one_site_function_test_case.this_log.lower(), self.test_id + ". Blad znalezienia podanej spolki.")
        if "usunieto strone" not in self.remove_one_site_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("usunieto strone", self.remove_one_site_function_test_case.this_log.lower(), self.test_id + ". Brak informacji o usunieciu spolki.")

        self.countdown_function_3.start()
        first = True
        while not self.countdown_function_3.finished:
            if first:
                self.look_function_test_case.start()
                first = False
            if self.look_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_3)
        self.the_log += self.look_function_test_case.this_log
        if not self.look_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_function_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji pokazywania spolek.")
        if self.remove_one_site_function_test_case.the_data.replace("/remove-", "")[1:-1] in self.look_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertNotIn(self.remove_one_site_function_test_case.the_data.replace("/remove-", "")[1:-1], self.look_function_test_case.this_log,
                             self.test_id + ". Blad poprawnego usuniecia spolki.")

    def test_usuwania_stron_2_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.clear_function_test_case.start()
                first = False
            if self.clear_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.clear_function_test_case.this_log
        if self.clear_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertFalse(self.clear_function_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji usuwania spolek, brak prosby o potwierdzenie.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.deletion_approval_test_case.start()
                first = False
            if self.deletion_approval_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.deletion_approval_test_case.this_log
        if not self.deletion_approval_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.deletion_approval_test_case.finished, self.test_id + ". Blad przy potwierdzeniu usuniecia.")
        if "wyczyszczono" not in self.deletion_approval_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("wyczyszczono", self.deletion_approval_test_case.this_log.lower(), self.test_id + ". Brak informacji o wyczyszczeniu bazy.")

        self.countdown_function_3.start()
        first = True
        while not self.countdown_function_3.finished:
            if first:
                self.look_function_test_case.start()
                first = False
            if self.look_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_3)
        self.the_log += self.look_function_test_case.this_log
        if not self.look_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_function_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji pokazywania spolek.")
        if "nie podano" not in self.look_function_test_case.this_log.lower():
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("nie podano", self.look_function_test_case.this_log.lower(), self.test_id + ". Blad poprawnego usuniecia wszystkich spolek.")

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
        self.look_function_test_case = None
        self.remove_one_site_function_test_case = None
        self.clear_function_test_case = None
        self.deletion_approval_test_case = None
